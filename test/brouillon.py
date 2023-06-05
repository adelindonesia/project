## Set up
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from datetime import datetime
import time


import pandas as pd

options = Options()
options.add_experimental_option("detach", True)

path = "C:\Program Files (x86)\chromedriver.exe"

# driver = webdriver.Chrome(path, options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.booking.com/")
driver.maximize_window()
driver.implicitly_wait(15)

pop_up_element = driver.find_element(
    By.ID, "onetrust-accept-btn-handler"
).click()


flights = driver.find_element(By.LINK_TEXT,"Flights" )
flights.click()


def dep_country_chooser(dep_city):
    fly_from_box = driver.find_element(By.CSS_SELECTOR, "button[data-ui-name='input_location_from_segment_0']")
    time.sleep(3)
    fly_from_box.click()
    fly_clear = driver.find_element(By.CSS_SELECTOR, ".css-rh2lq6")
    time.sleep(3)
    fly_clear.click()
    fly_from = driver.find_element(By.CSS_SELECTOR, "input[data-ui-name='input_text_autocomplete']")
    time.sleep(3)
    fly_from.send_keys('  ' + dep_city)
    time.sleep(3)
    fly_from_airport = driver.find_element(By.CSS_SELECTOR, "input[name='AIRPORTBRU']")
    time.sleep(3)
    fly_from_airport.click()

def arrival_country_chooser(arr_city):
    fly_to_box = driver.find_element(By.CSS_SELECTOR, "button[data-ui-name='input_location_to_segment_0']")
    time.sleep(3)
    fly_to_box.click()
    fly_to = driver.find_element(By.CSS_SELECTOR, "input[data-ui-name='input_text_autocomplete']")
    time.sleep(3)
    fly_to.send_keys('  ' + arr_city)
    time.sleep(3)
    fly_to_airport = driver.find_element(By.CSS_SELECTOR, "input[name='AIRPORTCGK']")
    time.sleep(3)
    fly_to_airport.click()

def round_trip_date_chooser(css_from_date, css_to_date):
    date_roundtrip_click = driver.find_element(By.CSS_SELECTOR, 'button[data-ui-name="button_date_segment_0"]')
    date_roundtrip_click.click()
    arrow = driver.find_element(By.CSS_SELECTOR, 'button[class="Actionable-module__root___lQCcK Button-module__root___puEjU Button-module__root--variant-tertiary___MhiYJ Button-module__root--icon-only___uhCdT Button-module__root--size-large___Oef9C Button-module__root--wide-false___ngEa+ Button-module__root--variant-tertiary-neutral___zGwxJ Calendar-module__control___5hEew Calendar-module__control--next___N9ipu"]')
    arrow.click()
    dep_date_button = driver.find_element(By.CSS_SELECTOR, css_from_date)
    dep_date_button.click()
    arr_date_button = driver.find_element(By.CSS_SELECTOR, css_to_date)
    arr_date_button.click()
    time.sleep(3)
    search_click = driver.find_element(By.CSS_SELECTOR, 'button[data-ui-name="button_search_submit"]')
    search_click.click()


def airline_chooser(airline_1, airline_2):
    # time.sleep(2)
    # driver.execute_script("window.scrollTo(0,400)")
    time.sleep(2)
    ticket_type = driver.find_element(By.CSS_SELECTOR, ".Link-module__root--variant-primary___skVxI, .Link-module__root--variant-secondary___IJWjg")
    ticket_type.click()
    time.sleep(2)
    element_to_hover_over = driver.find_element(By.CSS_SELECTOR, "[data-testid='search_filter_airline_" + airline_1 + "']")
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    time.sleep(2)
    air_1 = driver.find_element(By.CSS_SELECTOR, 'button[class="Actionable-module__root___lQCcK Link-module__root___Jo24k Link-module__root--variant-primary___skVxI"]')
    air_1.click()
    air_2 = driver.find_element(By.CSS_SELECTOR, "[data-testid='search_filter_airline_" + airline_2 + "']" )
    air_2.click()


def flight_details(details = ".css-4o3ibe"):
    price_roundtrip_ticket = []     # price of the roundtrip ticket in euro/person
    airline_company = []            # name of the airline company

    # out_dep_city = []               # outbound departure city
    # out_dep_time = []               # outbound flight departure time
    # out_dep_date = []               # outbound flight departure date
    # out_dep_fly_time = []           # lenght outbound flight from departure city to stopover city
    # out_stop_over_arr_date = []     # outbound stopover date arrival
    # out_stop_over_city = []         # outbound stopover city
    # out_stop_over_time = []         # length of the outbound stopover
    # out_stop_over_dep_date = []     # outbound stopover date departure
    # out_arr_city = []               # outbound arrival city
    # out_arr_time = []               # outbound flight arrival time
    # out_arr_date = []               # outbound flight arrival date
    # out_arr_fly_time = []           # length outbound flight from stopover city to arrival 
    
    # in_dep_time = []                # inbound flight departure time
    # in_dep_date = []                # inbound flight departure date
    # in_dep_fly_time = []            # length of inbound flight from departure city to stopover city
    # in_stop_over_arr_date = []      # inbound stopover date arrival
    # in_stop_over_city = []          # inbound stopover city
    # in_stop_over_time = []          # length of the inbound stopover
    # in_stop_over_dep_date = []      # inbound stopover date departure
    # in_arr_time = []                # inbound flight arrival time
    # in_arr_date = []                # inbound flight arrival date
    # in_arr_fly_time = []            # length of inbound flight from stopover city to arrival city

    # personal_item = []              # can take value one if it is included in the bagage or zero
    # carry_on_bag = []               # maximum weight of carry-on bag
    # checked_bag = []                # maximum weight of checked bag

    info = driver.find_elements(By.CSS_SELECTOR, details)

    for i in range(0, len(info)-1):
        price_roundtrip_ticket.append(
            info[0].find_element(
            By.XPATH, f"//*[@id='flight-card-{i}']/div/div/div[2]/div[2]/div/div[1]/div/div/div"
        ).text
        )
    
        airline_company.append(
            info[0].find_element(
            By.XPATH, f"//*[@id='flight-card-{i}']/div/div/div[1]/div[3]/div/div/div"
            ).text
        )

    df = pd.DataFrame(list(zip(price_roundtrip_ticket, airline_company)), columns=["Price", "Airline Company"])
    return(df)

        

dep_country_chooser("brussels")
arrival_country_chooser("jakarta")
round_trip_date_chooser(css_from_date='span[data-date="2023-08-01"]', css_to_date='span[data-date="2023-08-15"]')
airline_chooser(airline_1="Lufthansa", airline_2="Qatar Airways")
flight_details(details = ".css-4o3ibe")