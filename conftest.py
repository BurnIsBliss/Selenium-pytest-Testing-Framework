import pytest

from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox", help="Specify the browser name where you wish to run your tests."
    )

@pytest.fixture(scope='class')
def setUp(request):
    browserName = request.config.getoption("--browser_name")
    if browserName.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browserName.lower() == "firefox":
        driver = webdriver.Firefox()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
