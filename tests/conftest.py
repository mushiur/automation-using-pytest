import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup():
    s = Service("../driver/chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    print("Launching chrome browser ..........")
    return driver
