import Expedia.constants as cst
import os
from selenium import webdriver

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class Expedia(webdriver.Chrome):
    """
    Provides a mechanism to write tests against Chrome
    
    ...

    Attributes
    ----------

    """

    def __init__(self, driver_path=r"C:\Program Files (x86)\chromedriver.exe", teardown = False):
        """
        Initializes a new instance of the ChromeDriver class using the specified path to the 
        directory containing ChromeDriver.exe.

        Parameters
        ----------
        driver_path : obj.
                        path of the webdriver in local
        
        teardown : False or True.
                    optional method to help teard down testing environment
        
        Returns
        -------
        None

        """
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Expedia, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
    
    def __exit__(self, exc_type, exc, traceback):
        """
        This function will shut down the Chrome browser,
        once the running file is finished if teardown=True.

        Parameters
        ----------
        exc_type : str, optional.
                    indicates class of exception

        exception_value : str, optional.
                            indicates type of exception
        
        traceback : str, optional.
                    traceback is a report which has all of 
                    the information needed to solve the exception.
        
        Returns
        -------
        None

        """
        if self.teardown:
            self.quit()

    def land_first_page(self):
        """
        Gets or sets the URL the browser is currently displaying
        which is the main page of Expedia.
        
        Parameters
        ----------
        self : instance of the webdriver

        Returns
        -------
        None

        """
        self.get(cst.BASE_URL)

    def close_pop_up(self):
        pop_up_element = self.find_element(
            By.Name, "close"
        )
        pop_up_element.click()






# flights = driver.find_element(By.LINK_TEXT, "Flights")
# flights.click()

# one_way = driver.find_element(By.LINK_TEXT, "One-way")
# one_way.click()

# destination_from = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Leaving from']")
# destination_from.click()

# input_dest_from = driver.find_element(By.ID, "location-field-leg1-origin").send_keys("Brussels")
# input_dest_form_click = driver.find_element(
#     By.CSS_SELECTOR, "button[aria-label='Brussels (BRU - Brussels-National) Belgium]"
#     ).click()



