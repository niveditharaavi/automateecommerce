import pytest
from selenium import webdriver
from Config.config import TestData
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.SignInPage import SignInPage
from pageObjects.top_menu import TopMenu


@pytest.fixture(params=["chrome"],scope='class')
def setup(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    # if request.params == "firefox":
    #     web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    web_driver.get(TestData.BASE_URL)
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield web_driver
    web_driver.close()



