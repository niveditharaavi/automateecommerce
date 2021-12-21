from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TopMenu:
    def __init__(self, driver):
        self.driver = driver

    @property
    def signin_link(self):
        search_string = "//a[@class='login']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def signout_link(self):
        search_string = "//a[@class='logout']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))