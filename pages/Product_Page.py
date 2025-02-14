from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.WaitUtil import ExplicitWaitUtil

class product_page:
    def __init__(self,driver:WebDriver):
        self.driver= driver
        self.wait_util = ExplicitWaitUtil(self.driver)
        
    def add_product(self,product_name):
       product_xpath = f"//div[@class='inventory_item_name ' and text()='{product_name}']"
       self.wait_util.wait_for_element((By.XPATH,product_xpath))
       add_to_cart_xpath = f"{product_xpath}//ancestor::div[@class='inventory_item']//button"
       self.wait_util.wait_for_element((By.XPATH,add_to_cart_xpath),EC.element_to_be_clickable).click()

    def remove_product(self,product_name):
        remove_xpath = f"//div[@class='inventory_item_name ' and text() = '{product_name}']//ancestor::div[@class='inventory_item']//button[text()='Remove']"
        self.wait_util.wait_for_element((By.XPATH,remove_xpath),EC.element_to_be_clickable).click()
        
    def is_product_added(self,product_name):
        remove_xpath = f"//div[@class='inventory_item_name ' and text() = '{product_name}']//ancestor::div[@class='inventory_item']//button[text()='Remove']"
        return self.wait_util.wait_for_element((By.XPATH,remove_xpath),EC.presence_of_element_located)
    
    def is_product_removed(self,product_name):
        product_xpath = f"//div[@class='inventory_item_name ' and text()='{product_name}']"
        self.wait_util.wait_for_element((By.XPATH,product_xpath))
        add_to_cart_xpath = f"{product_xpath}//ancestor::div[@class='inventory_item']//button"
        self.wait_util.wait_for_element((By.XPATH,add_to_cart_xpath),EC.element_to_be_clickable).click()
        return self.wait_util.wait_for_element((By.XPATH,f"${add_to_cart_xpath}[text() = 'Add to cart']"),EC.presence_of_element_located)
    
    