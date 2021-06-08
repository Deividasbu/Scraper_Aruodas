from aruodas_scraper.scraper import Scraper
from bs4 import BeautifulSoup
import pandas as pd

scraper = Scraper()
main_url = "https://www.aruodas.lt/butu-nuoma/puslapis/1/"


def test_get_response():
    response = scraper.get_response(main_url)
    assert response.status_code == 200


def test_get_soup():
    soup = scraper.get_soup(scraper.get_response(main_url))
    assert isinstance(soup, BeautifulSoup)


def test_extract_info():
    scraped_data = []
    req = scraper.get_response(main_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    result = scraper.extract_info(soup, scraped_data)
    assert not len(result) == 0


def test_clean_data():
    scraped_data = []
    soup = scraper.get_soup(scraper.get_response(main_url))
    scraper.extract_info(soup, scraped_data)
    df = pd.DataFrame(scraped_data)
    filtered_df = scraper.clean_data(df)

    columns_after_filter = [
        "area",
        "rooms",
        "price",
        "price_pm",
        "city",
        "district",
        "floor",
        "floors_total",
    ]
    assert (filtered_df.columns == columns_after_filter).all()


def test_scrape_aruodas():
    df = scraper.scrape_aruodas(1)
    assert df.shape == (26,8)
