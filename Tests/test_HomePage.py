import pytest

from Utilities.baseClass import BaseClass
from pageObject.HomePage import homePage
from TestData.HomePageData import HomePageData

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homePageObj = homePage(self.driver)
        homePageObj.getName().clear()
        homePageObj.getName().send_keys(getData['firstName'])
        homePageObj.getEmail().clear()
        homePageObj.getEmail().send_keys(getData['lastName'])
        homePageObj.getCheckBox().click()
        self.selectOptionsByText(homePageObj.getGender(), getData['gender'])
        homePageObj.submitForm().click()

        alertText = homePageObj.getSuccessMessage().text

        assert "Success" in alertText
        self.driver.refresh()

    # @pytest.fixture(params=[('Lucy', 'Mane', 'Female'), ('Lance', 'Armstrong', 'Male')])
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

