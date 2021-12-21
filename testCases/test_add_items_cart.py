
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Actions.homepage import addition_of_an_item_to_cart
from pageObjects.HomePage import HomePage
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class Test_Cart:

    @pytest.mark.ui_workflows
    def test_add_items_to_cart(self):
        homepage = HomePage(self.driver)
        no_of_items_in_homepage = len(homepage.items_in_homepage)
        if no_of_items_in_homepage > 0:
            success_message = addition_of_an_item_to_cart(homepage, no_of_items_in_homepage)
            assert "Product successfully added to your shopping cart" in success_message.text, \
                "Success message is not seen when an item is added to cart "
            self.driver.save_screenshot("Screenshots/itemaddedwindow.png")
            homepage.cart_popup_window.click()

    @pytest.mark.ui_workflows
    def test_delete_items_from_cart(self):
        homepage = HomePage(self.driver)
        homepage.cart_link.click()
        try:
            search_string = "//table[@id='cart_summary']//tbody//tr"
            items_in_cart_page = WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, search_string)))
            if len(items_in_cart_page) > 0:
                search_string = "//table[@id='cart_summary']//tbody//tr[1]//td[@data-title='Delete']//a"
                delete_button = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, search_string)))
                delete_button.click()
                search_string = "//p[@class='alert alert-warning']"
                alert_message = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, search_string)))
                assert "Your shopping cart is empty." in alert_message.text
        except TimeoutException:
            print("There is no item in shopping cart")
