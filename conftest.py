from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome")
    
@pytest.fixture(scope="class",autouse=True)
def selenuimdriver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        service = Service('/opt/homebrew/bin/chromedriver')
        driver = webdriver.Chrome(service=service)
        request.cls.driver = driver
    elif browser == "firefox":
        service = Service('/opt/homebrew/bin/geckodriver')
        driver = webdriver.Firefox(service=service)
        request.cls.driver = driver
        
    else:
        raise ValueError(f"Brower '${browser} is not supported.'")
        
    yield
    driver.quit()
    
@pytest.fixture(scope="class",autouse=True)
def test_browser(request):
    browser = request.config.getoption("--browser")
    return browser
