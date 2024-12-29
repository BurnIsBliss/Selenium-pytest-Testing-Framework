from selenium.webdriver.common.by import By
from pageObject.CheckOutPage import CheckOutPage

class homePage:
    shop = (By.CSS_SELECTOR, 'a[href*=shop]')

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*homePage.shop).click()
        return CheckOutPage(self.driver)
