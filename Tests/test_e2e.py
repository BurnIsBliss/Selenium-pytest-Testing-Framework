from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.baseClass import BaseClass
from pageObject.HomePage import homePage

class TestOne(BaseClass):

    def test_e2e(self):
        HPage = homePage(self.driver)
        checkoutPage = HPage.shopItems()
        cards = checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i += 1
            cardText = card.text
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()
        
        checkoutPage.getCheckOutButton().click()

        confirmPageObj = checkoutPage.getFinalCheckoutButton()
        confirmPageObj.getCountryField().send_keys('aus')

        self.verifyLinkPresence('Austria')
        self.driver.find_element(By.LINK_TEXT, 'Austria').click()

