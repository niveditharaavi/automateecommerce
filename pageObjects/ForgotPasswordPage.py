from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def email_address_textfield(self):
        search_string = "//form[@id='form_forgotpassword']//input[@name='email']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def retrieve_password_button(self):
        search_string = "//span[contains(text(),'Retrieve Password')]/parent::button"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))
