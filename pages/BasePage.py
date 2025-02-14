from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def navigate(driver:WebDriver,url:str) -> None:
        try:
            driver.get(url=url)
        except Exception as e:
            raise e