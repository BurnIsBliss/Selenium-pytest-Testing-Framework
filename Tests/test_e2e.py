from selenium.webdriver.common.by import By

from Utilities.baseClass import BaseClass
from pageObject.HomePage import homePage

class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        HPage = homePage(self.driver)
        checkoutPage = HPage.shopItems()
        log.info('Getting all the card titles.')
        cards = checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i += 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()
        
        checkoutPage.getCheckOutButton().click()

        confirmPageObj = checkoutPage.getFinalCheckoutButton()
        log.info('Entering country name as "aus".')
        confirmPageObj.getCountryField().send_keys('aus')

        self.verifyLinkPresence('Austria')
        self.driver.find_element(By.LINK_TEXT, 'Austria').click()

        confirmPageObj.getCheckbox().click()
        confirmPageObj.getPurchaseButton().click()
        message = confirmPageObj.getSuccessText().text
        log.info('Displayed message is {}'.format(message))
        assert "Success!" in message

