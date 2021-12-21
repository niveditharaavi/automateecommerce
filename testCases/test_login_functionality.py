import pytest

from pageObjects.ForgotPasswordPage import ForgotPasswordPage
from pageObjects.SignInPage import SignInPage
from pageObjects.top_menu import TopMenu
from Config.config import TestData
from Utilities.customLogger import LogGen


class Test_Login:
    logger = LogGen.loggen()

    @pytest.mark.ui_workflows
    def test_login_with_incorrect_password(self, setup):
        self.driver = setup
        topmenu = TopMenu(self.driver)
        topmenu.signin_link.click()
        signin = SignInPage(self.driver)
        signin.signin_email_textfield.send_keys(TestData.USERNAME)
        signin.password_textfield.send_keys("xyzjhfdjfh")
        signin.sign_in_button.click()
        alert = self.driver.find_element_by_xpath("//div[@class='alert alert-danger']//li")
        assert "Authentication failed." in alert.text

    @pytest.mark.ui_workflows
    def test_login_with_unregistered_email(self, setup):
        self.driver = setup
        topmenu = TopMenu(self.driver)
        topmenu.signin_link.click()
        signin = SignInPage(self.driver)
        signin.signin_email_textfield.send_keys("abc@gmail.com")
        signin.password_textfield.send_keys("xyzxyz")
        signin.sign_in_button.click()
        alert = self.driver.find_element_by_xpath("//div[@class='alert alert-danger']//li")
        assert "Authentication failed." in alert.text

    @pytest.mark.ui_workflows
    def test_forgot_password(self, setup):
        self.driver = setup
        topmenu = TopMenu(self.driver)
        topmenu.signin_link.click()
        signin = SignInPage(self.driver)
        signin.signin_email_textfield.send_keys(TestData.USERNAME)
        signin.forgot_password_link.click()
        forgotpassword = ForgotPasswordPage(self.driver)
        assert self.driver.title == "Forgot your password - My Store"
        forgotpassword.email_address_textfield.send_keys(TestData.USERNAME)
        forgotpassword.retrieve_password_button.click()
        alert = self.driver.find_element_by_xpath("//p[@class='alert alert-success']")
        assert f"A confirmation email has been sent to your address: {TestData.USERNAME}" in alert.text

    @pytest.mark.ui_workflows
    def test_login_success(self, setup):
        self.logger.info("********Test_Login********")
        self.logger.info("******* Test signin with valid credentials******")
        self.driver = setup
        topmenu = TopMenu(self.driver)
        topmenu.signin_link.click()
        signin = SignInPage(self.driver)
        self.logger.info("Enter username and password")
        signin.signin_email_textfield.send_keys(TestData.USERNAME)
        signin.password_textfield.send_keys(TestData.PASSWORD)
        signin.sign_in_button.click()
        assert self.driver.title == "My account - My Store"
        self.logger.info("Signed in successfully")
