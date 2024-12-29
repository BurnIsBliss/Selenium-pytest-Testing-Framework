from selenium.webdriver.common.by import By
from pageObject.CheckOutPage import CheckOutPage

class homePage:
    shop = (By.CSS_SELECTOR, 'a[href*=shop]')
    name = (By.CSS_SELECTOR, '[name="name"]')
    email = (By.NAME, 'email')
    checkBox = (By.ID, 'exampleCheck1')
    selectGender = (By.ID, 'exampleFormControlSelect1')
    submitButton = (By.XPATH, "//input[@class='btn btn-success']")
    successMessage = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*homePage.shop).click()
        return CheckOutPage(self.driver)

    def getName(self):
        return self.driver.find_element(*homePage.name)
    
    def getEmail(self):
        return self.driver.find_element(*homePage.email)
    
    def getCheckBox(self):
        return self.driver.find_element(*homePage.checkBox)
    
    def getGender(self):
        return self.driver.find_element(*homePage.selectGender)
    
    def submitForm(self):
        return self.driver.find_element(*homePage.submitButton)
    
    def getSuccessMessage(self):
        return self.driver.find_element(*homePage.successMessage)

    

    
