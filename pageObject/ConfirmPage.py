from selenium.webdriver.common.by import By

class ConfirmationPage:

    countryInputField = (By.ID, 'country')
    termsAndConditionsCheckbox = (By.XPATH, '//div[@class="checkbox checkbox-primary"]')
    purchaseButton = (By.CSS_SELECTOR, 'input[class*="btn-success"]')
    successText = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver
    
    def getCountryField(self):
        return self.driver.find_element(*ConfirmationPage.countryInputField)
    
    def getCheckbox(self):
        return self.driver.find_element(*ConfirmationPage.termsAndConditionsCheckbox)
    
    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmationPage.purchaseButton)
    
    def getSuccessText(self):
        return self.driver.find_element(*ConfirmationPage.successText)