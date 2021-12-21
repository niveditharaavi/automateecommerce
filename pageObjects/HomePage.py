from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def popular_tab_link(self):
        search_string = "//a[text()='Popular']"
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def best_sellers_tab_link(self):
        search_string = "//a[text()='Best Sellers']"
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def items_in_homepage(self):
        search_string = "//ul[@id='homefeatured']//li"
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, search_string)))

    @property
    def cart_link(self):
        search_string = "//a[@title='View my shopping cart']"
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def cart_popup_window(self):
        search_string = "//span[@title='Close window']"
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))




