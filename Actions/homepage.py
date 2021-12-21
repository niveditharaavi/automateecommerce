from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def addition_of_an_item_to_cart(homepage, no_of_items_in_homepage):
    for i in range(1, no_of_items_in_homepage + 1):
        search_string = "//ul[@id='homefeatured']//li[" + str(i) + "]"
        item = WebDriverWait(homepage.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, search_string)))
        a = ActionChains(homepage.driver)
        a.move_to_element(item).perform()
        search_string = f"//ul[contains(@class,'active')]//a[@title='Add to cart' and @data-id-product='{i}']"
        add_to_cart_button = WebDriverWait(homepage.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, search_string)))
        add_to_cart_button.click()
        break
    search_string = "//div[contains(@class,'layer_cart_product')]//h2"
    success_message = WebDriverWait(homepage.driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, search_string)))
    return success_message
