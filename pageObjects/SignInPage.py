from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def signin_email_textfield(self):
        """The email address textfield present under already registered section in sign in page"""
        search_string = "//form[@id='login_form']//input[@id='email']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def password_textfield(self):
        """The password textfield present under already registered secton in sign in page"""
        search_string = "//form[@id='login_form']//input[@id='passwd']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def create_email_textfield(self):
        """The email address textfield present under create an account section in sign in page"""
        search_string = "//form[@id='create-account_form']//input[@id='email_create']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def create_account_button(self):
        """The create account button present under create an account section in sign in page"""
        search_string = "//button[@id='SubmitCreate']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def sign_in_button(self):
        """The create account button present under create an account section in sign in page"""
        search_string = "//button[@id='SubmitLogin']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def forgot_password_link(self):
        search_string = "//a[@title='Recover your forgotten password']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))
