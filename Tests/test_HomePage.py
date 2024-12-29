from Utilities.baseClass import BaseClass
from pageObject.HomePage import homePage

class TestHomePage(BaseClass):

    def test_formSubmission(self):
        homePageObj = homePage(self.driver)
        homePageObj.getName().send_keys('Alan')
        homePageObj.getEmail().send_keys('alan@abc.xyz')
        homePageObj.getCheckBox().click()
        self.selectOptionsByText(homePageObj.getGender(), 'Male')
        homePageObj.submitForm().click()

        alertText = homePageObj.getSuccessMessage().text

        assert "Success" in alertText