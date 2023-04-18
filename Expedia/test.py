import project_test.constants as cst
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Expedia(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Program Files (x86)\chromedriver.exe"):
        self.driver_path = driver_path
        super(Expedia, self).__init__
    
    def land_first_page(self):
        self.get("https://www.expedia.com/")







options = Options()
options.add_experimental_option("detach", True)

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path, options=options)
driver.get("https://www.expedia.com/")
driver.implicitly_wait(30)

close_pop_up = driver.find_element(By.NAME, "close")
close_pop_up.click()

flights = driver.find_element(By.LINK_TEXT, "Flights")
flights.click()

one_way = driver.find_element(By.LINK_TEXT, "One-way")
one_way.click()

destination_from = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Leaving from']")
destination_from.click()

input_dest_from = driver.find_element(By.ID, "location-field-leg1-origin").send_keys("Brussels")
input_dest_form_click = driver.find_element(
    By.CSS_SELECTOR, "button[aria-label='Brussels (BRU - Brussels-National) Belgium]"
    ).click()



