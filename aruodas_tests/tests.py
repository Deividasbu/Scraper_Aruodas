import pytest
from aruodas_scraper.scraper import Scraper
import pandas as pd
from bs4 import BeautifulSoup

scraper = Scraper()
example_url = 'https://www.aruodas.lt/butu-nuoma-vilniuje-zirmunuose-m-katkaus-g-isnuomojamas-modernus-naujai-irengtas-butas-4-849055/'


def test_get_response():
    response = scraper.get_response(example_url)
    assert response.status_code == 200
