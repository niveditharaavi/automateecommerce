from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import TestData
from pageObjects.RegistrationPage import RegistrationPage
from pageObjects.SignInPage import SignInPage
from pageObjects.top_menu import TopMenu
from selenium.webdriver.support import expected_conditions as EC


class Test_Registration:

    def test_registration_with_invalid_zipcode(self, setup):
        self.driver = setup
        topmenu = TopMenu(self.driver)
        topmenu.signin_link.click()
        signin = SignInPage(self.driver)
        signin.create_email_textfield.send_keys("userxynnnnnz@abc.com")
        signin.create_account_button.click()
        registration = RegistrationPage(self.driver)
        registration.female_gender_radio_button.click()
        registration.firstname_textfield.send_keys("justforfun")
        registration.lastname_textfield.send_keys("dude")
        registration.password_textfield.send_keys("Awesome123")
        day = Select(self.driver.find_element_by_name('days'))
        day.select_by_value('16')
        month = Select(self.driver.find_element_by_name('months'))
        month.select_by_value('11')
        year = Select(self.driver.find_element_by_name('years'))
        year.select_by_value('2015')
        registration.address_textfield.send_keys("501 west college street")
        registration.city_textfield.send_keys("carbondale")
        state = Select(self.driver.find_element_by_id('id_state'))
        state.select_by_visible_text('Illinois')
        registration.zipcode_textfield.send_keys('629019878978768687')
        registration.mobile_phone_textfield.send_keys('9000789067')
        registration.register_button.click()
        alert = self.driver.find_element_by_xpath("//div[@class='alert alert-danger']//li[1]")
        assert "postcode is too long. Maximum length: 12" in alert.text,"No alert message is seen when " \
                                                                        "incorrect zipcode is given "

    def test_registration_with_missing_mandatory_fields(self, setup):
        self.driver = setup
        topmenu = TopMenu(self.driver)
        topmenu.signin_link.click()
        signin = SignInPage(self.driver)
        signin.create_email_textfield.send_keys("userxynnnnnz@abc.com")
        signin.create_account_button.click()
        registration = RegistrationPage(self.driver)
        registration.firstname_textfield.send_keys("justforfun")
        registration.lastname_textfield.send_keys("dude")
        registration.address_textfield.send_keys("501 west college street")
        state = Select(self.driver.find_element_by_id('id_state'))
        state.select_by_value('4')
        registration.zipcode_textfield.send_keys('62901')
        registration.mobile_phone_textfield.send_keys('9000789067')
        registration.register_button.click()
        alert = self.driver.find_element_by_xpath("//div[@class='alert alert-danger']//ol")
        assert "passwd is required" in alert.text
        assert "city is required" in alert.text

    def test_register_with_registered_email(self, setup):
        self.driver = setup
        topmenu = TopMenu(self.driver)
        topmenu.signin_link.click()
        signin = SignInPage(self.driver)
        signin.create_email_textfield.send_keys(TestData.USERNAME)
        signin.create_account_button.click()
        search_string = "//div[@class='alert alert-danger']//ol"
        alert = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, search_string)))
        assert "An account using this email address has already been registered." in alert.text

    def test_registration_success(self, setup):
        self.driver = setup
        topmenu = TopMenu(self.driver)
        topmenu.signin_link.click()
        signin = SignInPage(self.driver)
        signin.create_email_textfield.send_keys("usernijkrrrrrrrrxyz@abc.com")
        signin.create_account_button.click()
        registration = RegistrationPage(self.driver)
        registration.female_gender_radio_button.click()
        registration.firstname_textfield.send_keys("justforfun")
        registration.lastname_textfield.send_keys("dude")
        registration.password_textfield.send_keys("Awesome123")
        day = Select(self.driver.find_element_by_name('days'))
        day.select_by_value('16')
        month = Select(self.driver.find_element_by_name('months'))
        month.select_by_value('11')
        year = Select(self.driver.find_element_by_name('years'))
        year.select_by_value('2015')
        registration.address_textfield.send_keys("501 west college street")
        registration.city_textfield.send_keys("carbondale")
        state = Select(self.driver.find_element_by_id('id_state'))
        state.select_by_visible_text('Illinois')
        registration.zipcode_textfield.send_keys('62901')
        registration.mobile_phone_textfield.send_keys('9000789067')
        registration.register_button.click()
        self.driver.save_screenshot("Screenshots/myaccountpage.png")
        assert self.driver.title == "My account - My Store", "Failed to open my account page after " \
                                                             "registration "
