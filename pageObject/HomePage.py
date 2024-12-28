from selenium.webdriver.common.by import By

class homePage:
    shop = (By.CSS_SELECTOR, 'a[href*=shop]')

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
       return self.driver.find_element(*homePage.shop)
