from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from utils.WaitUtil import ExplicitWaitUtil
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait_util = ExplicitWaitUtil(self.driver)
        self.username_field = (By.ID,"user-name")
        self.password_field = (By.ID,"password")
        self.login_button = (By.ID,"login-button")
        self.error_message = (By.XPATH,"//h3[@data-test='error'] | //button[@data-test='error-button'] | //h3[text()='Epic sadface: Sorry, this user has been locked out.']")
        
    def enter_username(self,username):
        """
        This method is designed to pass username the particular website
        Args:
            username (str): username accepts only string
        """
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)
    
    def enter_password(self,password):
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)
        
    def login(self):
        self.driver.find_element(*self.login_button).click()
        
    def is_logged_in(self):
        try:
            return self.wait_util.wait_for_element((By.XPATH,"//span[@data-test='title']")).is_displayed()
        except :
            return False
                
    def is_error_message_displayed(self):
        try:
            element = self.wait_util.wait_for_element(self.error_message, EC.visibility_of_element_located(self.error_message))
            print(f"Error message element found: {element}")  # Debugging log
            return element.is_displayed()
        except Exception as e:
            print(f"Error while checking for error message: {e}")
            return False 