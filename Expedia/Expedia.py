import constants as cst
import os
from selenium import webdriver

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class Expedia(webdriver.Chrome):
#     """
#     Provides a mechanism to write tests against Chrome
    
#     ...

#     Attributes
#     ----------

#     """

#     def __init__(self, driver_path = r"C:\\Program Files (x86)\\chromedriver.exe", teardown = False):
#         """
#         Initializes a new instance of the ChromeDriver class using the specified path to the 
#         directory containing ChromeDriver.exe.

#         Parameters
#         ----------
#         driver_path : obj.
#                         path of the webdriver in local
        
#         teardown : False or True.
#                     optional method to help teard down testing environment
        
#         Returns
#         -------
#         None

#         """
#         self.__driver_path = driver_path
#         self.__teardown = teardown
#         self.add_env_var()                  # add chromedriver to system environment variables
#         super(__class__, self).__init__()   # create an instance of webdriver.Chrome
#         self.implicitly_wait(30)
#         self.maximize_window()

#     # =========================================================================
#     @property
#     def driver_path(self):
#         return self.__driver_path

#     @driver_path.setter
#     def driver_path(self, driver_path = r"C:\\Program Files (x86)\\chromedriver.exe"):
#         self.__driver_path = driver_path
#     # =========================================================================

#     # =========================================================================
#     @property
#     def teardown(self):
#         return self.__teardown

#     @teardown.setter
#     def teardown(self, teardown = False):
#         self.__teardown = teardown
#     # =========================================================================

#     # =========================================================================
#     @staticmethod
#     def add_env_var(driver_path = r"C:\\Program Files (x86)\\chromedriver.exe"):
#         os.environ["PATH"] += ";" + driver_path
#     # =========================================================================
    
#     def __exit__(self):
#         """
#         This function will shut down the Chrome browser,
#         once the running file is finished if teardown=True.

#         Parameters
#         ----------
#         exc_type : str, optional.
#                     indicates class of exception

#         exception_value : str, optional.
#                             indicates type of exception
        
#         traceback : str, optional.
#                     traceback is a report which has all of 
#                     the information needed to solve the exception.
        
#         Returns
#         -------
#         None

#         """
#         if self.teardown:
#             self.quit()

#     def land_first_page(self):
#         """
#         Gets or sets the URL the browser is currently displaying
#         which is the main page of Expedia.
        
#         Parameters
#         ----------
#         self : instance of the webdriver

#         Returns
#         -------
#         None

#         """

#         self.get(cst.BASE_URL)
#         self.close_pop_up()

#         while(True):
#             pass

#     # def close_pop_up(self):
#     #     pop_up_element = self.find_element(
#     #         by = self.By.NAME,
#     #         value ="close"
#     #     )
#     #     pop_up_element.click()

#     # # =========================================================================
#     # @classmethod
#     # def close_pop_up(cls):
#     #     pop_up_element = cls.find_element(
#     #         by = cls.By.NAME,
#     #         value ="close"
#     #     )
#     #     pop_up_element.click()
#     # # =========================================================================
#     # =========================================================================
#     def close_pop_up(self):
#         pop_up_element = super().find_element(
#             by = super().By.NAME,
#             value ="close"
#         )
#         pop_up_element.click()
#     # =========================================================================

# if __name__ == "__main__":
#     test = Expedia()
#     test.land_first_page()

# class Expedia(webdriver.Chrome):
#     def __init__(self, driver_path=r"C:\\Program Files (x86)\\chromedriver.exe", options = Options()) -> None:
#         self.__driver_path = driver_path
#         self.options = options
#         options.add_experimental_option("detach", True)
#         self.add_env_var()
#         super(__class__, self).__init__()
#         self.maximize_window()
    
#     # =================================================================================================================
#     @property
#     def driver_path(self):
#         return self.__driver_path

#     @driver_path.setter
#     def driver_path(self, driver_path = r"C:\\Program Files (x86)\\chromedriver.exe"):
#         self.__driver_path = driver_path
#     # =================================================================================================================

#     # =================================================================================================================
#     @staticmethod
#     def add_env_var(driver_path = r"C:\\Program Files (x86)\\chromedriver.exe"):
#         os.environ["PATH"] += ";" + driver_path
#     # =================================================================================================================
    
#     def land_first_page(self):
#        self.get(cst.BASE_URL)
#     #    self.close_pop_up() 
    
    # =========================================================================
    # def close_pop_up(self):
    #     pop_up_element = super().find_element(
    #         by = super().By.NAME,
    #         value ="close"
    #     )
    #     pop_up_element.click()
    # =========================================================================

if __name__ == "__main__":
    test = Expedia()
    test.land_first_page()








