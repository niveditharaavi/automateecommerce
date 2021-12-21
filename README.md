# automateecommerce
 Selenium Python framework for automating the ecommerce website 
pageObjects package contains pageobjects(locators) of all the pages ex:Homepage, Registrationpage ..
testCases package contains tests that checks the registration, Signin and items addition and deletion from the cart
Inoreder to run the tests , run the command 
pytest -v -s testCases/test_add_items_cart.py to run the tests in test_add_items_cart.py file
pytest -v -s testCases/test_login_functionality.py to run the tests in test_login_functionality.py file
pytest -v -s testCases/test_resgistration_page_functionality.py to run the tests in test_registration_page_functionality.py file
In order to run the tests with marker run pytest -v -m ui_workflows.  , all the tests that are marked with ui_workflows marker gets executed

I also attached the html files which are generated after execution by using command( pytest -v -s testCases/test_add_items_cart.py --html=cart.html)
The site is raising '508 Resource Limit is Reached Error' in the middle of executing the tests so the successful runs are there in the html file attached 
