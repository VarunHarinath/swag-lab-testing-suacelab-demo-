from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException


class ExplicitWaitUtil:
    def __init__(self,driver,timeout=10,poll_frequency=2):
        """
        Initialize the WaitHelper with driver and default timeout, poll_frequency, and ignored exceptions.
        """
        self.driver = driver
        self.time_out = timeout
        self.poll_frequency = poll_frequency
        self.ignored_exceptions = [NoSuchElementException,ElementNotVisibleException]
    
    def wait_for_element(self,locator,condition=EC.presence_of_element_located):
        """
        Waits for an element based on the specified condition.
        :param locator: Tuple for locating the element (e.g., (By.ID, "example_id")).
        :param condition: Expected condition (default: presence_of_element_located).
        :return: The WebElement if found.
        """
        wait = WebDriverWait(
            self.driver,
            self.time_out,
            self.poll_frequency,
            ignored_exceptions = self.ignored_exceptions
        )
        return wait.until(condition(locator))
        
        
        
        
        