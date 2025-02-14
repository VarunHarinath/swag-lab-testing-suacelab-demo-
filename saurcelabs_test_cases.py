import pytest
from pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage as basepage
from pages.Login_page import LoginPage
from pages.Product_Page import product_page

@pytest.mark.usefixtures("selenuimdriver")
class Test_Sauce_Labs:
    url = "https://www.saucedemo.com/"
    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.product_pg = product_page(self.driver)
        basepage.navigate(self.driver,self.url)
        
    def test_login_valild_user(self):
        try:    
            self.login_page.enter_username("standard_user")
            self.login_page.enter_password("secret_sauce")
            self.login_page.login()
            assert self.login_page.is_logged_in() , f"Login failed"
        except Exception as e :
            raise e
        
    def test_login_locked_out_user(self):
        try:
            self.login_page.enter_username("locked_out_user")
            self.login_page.enter_password("secret_sauce")
            self.login_page.login()
            assert self.login_page.is_error_message_displayed,"Failed with wrong credntials"
        except Exception as e:
            raise e
    
    def test_empty_login_user(self):
        try:
            self.login_page.enter_username("")
            self.login_page.enter_password("")
            self.login_page.login()
            assert self.login_page.is_error_message_displayed,"Failed to login with Empy Username and passwrod"
        except Exception as e:
            raise e
        
    def test_add_product(self): 
        try:
            self.login_page.enter_username("problem_user")
            self.login_page.enter_password("secret_sauce")
            self.login_page.login()
            self.product_pg.add_product("Sauce Labs Backpack")
            assert self.product_pg.is_product_added("Sauce Labs Backpack"), "Product was not added"
            self.product_pg.remove_product("Sauce Labs Backpack")
            assert self.product_pg.is_product_removed("Sauce Labs Backpack"), "Product was not removed"
            
        except Exception as e:
            raise e
            
    
    
        
    
    