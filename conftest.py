import configparser
import os

import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def config():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    _file = os.path.abspath(cur_dir) + "\\" + "configurations\\config.ini"
    parser = configparser.ConfigParser()
    parser.read(_file)
    return parser


@pytest.fixture(scope='function')
def driver(request):
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    _chromedriver = os.path.abspath(cur_dir) + "\\" + "driver\\chromedriver.exe"
    driver = webdriver.Chrome(_chromedriver)
    driver.maximize_window()

    def fin():
        driver.close()

    request.addfinalizer(fin)
    return driver
