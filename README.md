# Aruodas.lt Scraper
## General info:
This package scrapes the information about the rent of real estate listings in the Lithuania. The information is scraped from page [aruodas.lt](https://www.aruodas.lt/butu-nuoma/).  
Scraper collects the information about property's monthly price, price per square meter, area, number of rooms, floor, total floors, city and district. 

## Installation & Usage
1. Install
```sh
!pip install git+https://github.com/Deividasbu/Scraper_Aruodas
```
2. Import the package
```python
from aruodas_scraper.scraper import Scraper
```
3. Create the instance of the class
```python
scraper = Scraper()
```
4. Collect the data for further analysis without saving it
```python
scraper.scrape_aruodas(10)
```
5. Scrape and save the data
```python
scraper.save_to_csv(10, 'ten_pages_scraped')
```

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Deividasbu/Scraper-225/blob/main/LICENSE)
