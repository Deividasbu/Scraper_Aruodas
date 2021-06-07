from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
from random import randint


class Scraper:
    """
    A Scraper designed to scrape information about the rent of real estate listings
    from www.aruodas.lt page

    Parameters:
        pages = number of pages to scrape. Each page contains 26 listings

    Returns:
        Data Frame consisting of city, district, price, price per squared meter, rooms count, area,
        floor, floors_total
    """
    def __init__(self) -> None:
        self.headers = {
            "User Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
        }
        self.pages = 0

    def get_response(self, url: str) -> requests.Response:
        """
        Gets response from url provided
        :param url: url to get response
        :return: requests.Response
        """
        return requests.get(url, headers=self.headers)

    def extract_info(self, soup: BeautifulSoup, results_list) -> list:
        """
        Extracts information about the listing
        :param soup: BeautifulSoup object of the listing
        :param results_list: list containing information extracted
        :return: list with information extracted
        """
        listings = soup.select("tr.list-row")

        for listing in listings:
            data = {"address": [value.img['title'] for value in listing.find_all("td", {"class": "list-img"})],
                            "area": [value.text.strip() for value in listing.find_all("td", {"class": "list-AreaOverall"})],
                            "rooms": [value.text.strip() for value in listing.find_all("td", {"class": "list-RoomNum"})],
                            "price": [value.text.strip() for value in listing.find_all("span", {"class": "list-item-price"})],
                            "price_pm": [value.text.strip() for value in listing.find_all("span", {"class": "price-pm"})],
                            "floors": [value.text.strip() for value in listing.find_all("td", {"class": "list-Floors"})]}
            results_list.append(data)

        return results_list

    def clean_data(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Cleans extracted data
        :param dataframe: DataFrame to clean
        :return: cleaned DataFrame
        """
        data = dataframe
        data = data.apply(lambda x: x.explode())
        data = data.dropna()
        data['address'] = data['address'].str.split(",")
        data['address'] = data['address'].str[:2]
        data['city'], data['district'] = data['address'].str
        data = data.drop(columns="address")
        data['area'] = data['area'].astype(float)
        data['rooms'] = data['rooms'].astype(int)
        data['price'] = data['price'].str.replace(" ", "").str.replace("€", "").astype(int)
        data['price_pm'] = data['price_pm'].str.replace(" ", "").str.replace("€/m²", "").str.replace(",", ".").astype(
            float)
        data['floors'] = data['floors'].str.split('/')
        data['floor'], data['floors_total'] = zip(*data['floors'])
        data = data.drop(columns='floors')

        return data

    def scrape_aruodas(self, pages: int) -> pd.DataFrame:
        """
        Scrapes each listing from the website and returns the information
        :param pages: integer indicating number of pages to scrape
        :return: DataFrame containing information scraped
        """
        self.pages = pages

        scraped_data = []

        for page_no in range(0, pages):
            req = self.get_response(
                f"https://www.aruodas.lt/butu-nuoma/puslapis/{page_no}/"
            )
            soup = BeautifulSoup(req.text, 'html.parser')
            result = self.extract_info(soup, scraped_data)
            sleep(randint(1, 4))

        df = pd.DataFrame(scraped_data)
        df = self.clean_data(df)
        df = df[['city', 'district', 'price', 'price_pm', 'rooms', 'area',
                 'floor', 'floors_total']]

        return df
