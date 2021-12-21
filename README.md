# automateecommerce
 Selenium Python framework for automating the ecommerce website 
1)pageObjects package contains pageobjects(locators) of all the pages ex:Homepage, Registrationpage ..
2)testCases package contains tests that checks the registration, Signin and items addition and deletion from the cart
3)Inoreder to run the tests , run the command 
4)pytest -v -s testCases/test_add_items_cart.py to run the tests in test_add_items_cart.py file
5)pytest -v -s testCases/test_login_functionality.py to run the tests in test_login_functionality.py file
6)pytest -v -s testCases/test_resgistration_page_functionality.py to run the tests in test_registration_page_functionality.py file
7)In order to run the tests with marker run pytest -v -m ui_workflows.  , all the tests that are marked with ui_workflows marker gets executed

8)I also attached the html files which are generated after execution by using command( pytest -v -s testCases/test_add_items_cart.py --html=cart.html)
9)The site is raising '508 Resource Limit is Reached Error' in the middle of executing the tests so the successful runs are there in the html file attached 
