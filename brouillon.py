# Set up
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path, options=options)
driver.get("https://www.booking.com/")
driver.maximize_window()
driver.implicitly_wait(15)

pop_up_element = driver.find_element(
    By.ID, "onetrust-accept-btn-handler"
).click()


flights = driver.find_element(By.LINK_TEXT,"Flights" )
flights.click()


# ===========================================================================
destination_from_click = driver.find_element(
    By.CSS_SELECTOR, "button[data-ui-name='input_location_from_segment_0']"
    ).click() 

destination_from_change = driver.find_element(
    By.CSS_SELECTOR, ".css-rh2lq6"
).click()

destination_from_input = driver.find_element(
    By.CSS_SELECTOR, "input[data-ui-name='input_text_autocomplete']"
).send_keys("Brussels")

destination_from = driver.find_element(
    By.ID, "__bui-25"
).click()

# ===========================================================================
destination_to_click = driver.find_element(
    By.CSS_SELECTOR, "button[data-ui-name='input_location_to_segment_0']"
).click()

destination_from_input = driver.find_element(
    By.CSS_SELECTOR, "input[data-ui-name='input_text_autocomplete']"
).send_keys("Jakarta")

destination_from = driver.find_element(
    By.CSS_SELECTOR, "input[name='AIRPORTCGK']"
).click()
# ===========================================================================

date_roundtrip_click = driver.find_element(
    By.CSS_SELECTOR, 'button[data-ui-name="button_date_segment_0"]'
).click()

date_go_click = driver.find_element(
    By.CSS_SELECTOR, 'span[data-ui-name="calendar_cell_2023-06-01"]'
).click()

date_back_click = driver.find_element(
    By.CSS_SELECTOR, 'span[data-ui-name="calendar_cell_2023-06-15"]'
).click()

search_click = driver.find_element(
    By.CSS_SELECTOR, 'button[data-ui-name="button_search_submit"]'
).click()
# ==========================================================================

