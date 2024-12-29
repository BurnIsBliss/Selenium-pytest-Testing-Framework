from selenium.webdriver.common.by import By
from pageObject.ConfirmPage import ConfirmationPage

class CheckOutPage:

    cardTitle = (By.CSS_SELECTOR, '.card-title a')
    cardFooter = (By.CSS_SELECTOR, '.card-footer button')
    checkOutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    finalCheckoutButton = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)
    
    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)
    
    def getCheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOutButton)
    
    def getFinalCheckoutButton(self):
        self.driver.find_element(*CheckOutPage.finalCheckoutButton).click()
        return ConfirmationPage(self.driver)
