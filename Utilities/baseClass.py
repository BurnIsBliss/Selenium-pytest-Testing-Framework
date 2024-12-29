import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures('setUp')
class BaseClass:
    
    def verifyLinkPresence(self, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))
