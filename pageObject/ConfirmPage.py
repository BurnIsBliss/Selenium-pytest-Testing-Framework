from selenium.webdriver.common.by import By

class ConfirmationPage:

    countryInputField = (By.ID, 'country')

    def __init__(self, driver):
        self.driver = driver
    
    def getCountryField(self):
        return self.driver.find_element(*ConfirmationPage.countryInputField)