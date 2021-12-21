from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def page_heading_text(self):
        search_string = "//body[@id='my-account']//h1[@class='page-heading']"
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, search_string)))