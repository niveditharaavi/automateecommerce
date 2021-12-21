from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def male_gender_radio_button(self):
        search_string = "//label[text()='Title']//following-sibling::div//input[@value='1']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def female_gender_radio_button(self):
        search_string = "//label[text()='Title']//following-sibling::div//input[@value='2']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def firstname_textfield(self):
        search_string = "//input[@name='customer_firstname']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def lastname_textfield(self):
        search_string = "//input[@name='customer_lastname']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def password_textfield(self):
        search_string = "//input[@name='passwd']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def dob_days_dropdown_button(self):
        search_string = "//select[@name='days']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def dob_months_dropdown_button(self):
        search_string = "//select[@name='months']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def dob_years_dropdown_button(self):
        search_string = "//select[@name='years']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def your_address_firstname_textfield(self):
        search_string = "//input[@name='firstname']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def your_address_lastname_textfield(self):
        search_string = "//input[@name='lastname']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def address_textfield(self):
        search_string = "//input[@name='address1']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def city_textfield(self):
        search_string = "//input[@id='city']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def state_dropdown_button(self):
        search_string = "//select[@id='id_state']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def zipcode_textfield(self):
        search_string = "//input[@id='postcode']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))

    @property
    def mobile_phone_textfield(self):
        search_string = "//input[@id='phone_mobile']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))


    @property
    def register_button(self):
        search_string = "//button[@id='submitAccount']"
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))


















