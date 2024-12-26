import pytest

from selenium import webdriver

@pytest.fixture(scope='class')
def setUp(request):
    driver = webdriver.Chrome()
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
