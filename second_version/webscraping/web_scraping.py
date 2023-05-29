#!/usr/bin/env python
# coding: utf-8

# # WEB SCRAPING

# ## Setting-up

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import shutil

import datetime
import time

import pandas as pd

driver = webdriver.Chrome()
driver.implicitly_wait(5)


# ## Functions

# In[2]:


def navigate_to_url(driver=driver, url: str= "https://www.booking.com/") -> None:
    """
    This function navigates to the specified URL using the provided driver and maximizes the window.

    Args:
    -----
        driver : The web driver to use for navigation.
            (Default sets to 'driver')
    
        url (str): The URL to navigate to. 
            (Default sets to "https://www.booking.com/")
    
    Return:
    -------
        None
    """
    driver.get(url)
    driver.maximize_window()


# In[3]:


# def accept_coockies(driver = driver, popup_name: str = "onetrust-accept-btn-handler") -> None:
#     """
#     This function finds and clicks on an element with the specified ID to accept cookies.
    
#     Args:
#     -----
#     driver: The web driver to use for finding and clicking on the element. 
#           (Default is `driver`)
#     popup_name (str): The ID of the element to find and click on. 
#            (Default is "onetrust-accept-btn-handler")
    
#     Return:
#     -------
#     None
#     """

#     driver.find_element(By.ID, popup_name).click()


# In[4]:


def manage_coockies(driver = driver, popup_name: str = "onetrust-pc-btn-handler") -> None:
    """
    This function finds and clicks on an element with the specified ID to manage cookies. It then finds and clicks on a button with the text 'Confirm My Choices'.

    Args:
    -----
    driver : The web driver to use for finding and clicking on the elements.
    (Default sets to 'driver')
 
    popup_name (str): The ID of the element to find and click on. 
    (Default sets to "onetrust-pc-btn-handler")
 
    Return:
    -------
    None
    """
    
    driver.find_element(By.ID, popup_name).click()
    driver.find_element(By.XPATH, "//button[text()='Confirm My Choices']").click()


# In[5]:


def go_to_flights(driver = driver, name = "Flights"):
    driver.find_element(By.LINK_TEXT, name).click()


# In[6]:


def input_from_city_airport(driver = driver, city: str = "brussels", airport: str = "AIRPORTBRU") -> None:
    """
    This function finds and clicks on an element to input the departure city and airport. 
    It clears the input bar to avoid unwanted input, inputs the departure city and airport, 
    and clicks on the airport.

    Args:
    -----
    driver : The web driver to use for finding and clicking on the elements.
    (Default sets to 'driver')
 
    city (str): The departure city to input. 
    (Default sets to "brussels")
    
    airport (str): The departure airport to input. 
    (Default sets to "AIRPORTBRU")
 
    Return:
    -------
    None
    """
    driver.find_element(By.CSS_SELECTOR, "button[data-ui-name='input_location_from_segment_0']").click()

    # Clear bar to avoid unwanted input
    driver.find_element(By.CSS_SELECTOR, ".css-rh2lq6").click()

    # Input departure city
    fly_from = driver.find_element(By.CSS_SELECTOR, "input[data-ui-name='input_text_autocomplete']")
    fly_from.send_keys('  ' + city.lower())
    fly_from_airport = driver.find_element(By.CSS_SELECTOR, f"input[name='{airport.upper()}']")
    fly_from_airport.click()


# In[7]:


def input_to_city_airport(driver = driver, city: str = "new york", airport: str = "AIRPORTJFK") -> None:
    """
    This function finds and clicks on an element to input the departure city and airport. 
    It clears the input bar to avoid unwanted input, inputs the departure city and airport, 
    and clicks on the airport.

    Args:
    -----
    driver : The web driver to use for finding and clicking on the elements.
    (Default sets to 'driver')
 
    city (str): The departure city to input. 
    (Default sets to "jakarta")
    
    airport (str): The departure airport to input. 
    (Default sets to "AIRPORTCGK")
 
    Return:
    -------
    None
    """
    driver.find_element(By.CSS_SELECTOR, "button[data-ui-name='input_location_to_segment_0']").click()
    fly_to = driver.find_element(By.CSS_SELECTOR, "input[data-ui-name='input_text_autocomplete']")
    fly_to.send_keys('  ' + city.lower())
    fly_to_airport = driver.find_element(By.CSS_SELECTOR, f"input[name='{airport.upper()}']")
    fly_to_airport.click()


# In[8]:


def round_trip_date_chooser(driver=driver, css_from_date: str= 'span[data-date="2023-08-01"]', css_to_date: str='span[data-date="2023-08-15"]'):
    """
    This function finds and clicks on elements to choose the departure and arrival dates for a round trip. It clicks on the date button, clicks on the arrow to navigate to the desired month, clicks on the departure and arrival dates, and clicks on the search button.

    Args:
    -----
    driver : The web driver to use for finding and clicking on the elements.
    (Default sets to 'driver')
 
    css_from_date (str): The CSS selector for the departure date element. 
    (Default sets to 'span[data-date="2023-08-01"]')
    
    css_to_date (str): The CSS selector for the arrival date element. 
    (Default sets to 'span[data-date="2023-08-15"]')
 
    Return:
    -------
    None
    """
    date_roundtrip_click = driver.find_element(By.CSS_SELECTOR, 'button[data-ui-name="button_date_segment_0"]')
    date_roundtrip_click.click()
    arrow = driver.find_element(By.CSS_SELECTOR, 'button[class="Actionable-module__root___lQCcK Button-module__root___puEjU Button-module__root--variant-tertiary___MhiYJ Button-module__root--icon-only___uhCdT Button-module__root--size-large___Oef9C Button-module__root--wide-false___ngEa+ Button-module__root--variant-tertiary-neutral___zGwxJ Calendar-module__control___5hEew Calendar-module__control--next___N9ipu"]')
    arrow.click()
    dep_date_button = driver.find_element(By.CSS_SELECTOR, css_from_date)
    dep_date_button.click()
    arr_date_button = driver.find_element(By.CSS_SELECTOR, css_to_date)
    arr_date_button.click()
    search_click = driver.find_element(By.CSS_SELECTOR, 'button[data-ui-name="button_search_submit"]')
    search_click.click()
    search_click.click()

# In[9]:


# def airline_chooser(driver = driver, airline_1: str= "Lufthansa", airline_2: str="Swiss"):
def airline_chooser(driver = driver, airline_1: str= "Lufthansa"):

    """
    This function finds and clicks on elements to choose the desired airlines. 
    It sleeps for 2 seconds, clicks on the ticket type element, sleeps for 2 seconds, 
    hovers over the first airline element, sleeps for 2 seconds, 
    and clicks on the first and second airline elements.

    Args:
    -----
    driver : The web driver to use for finding and clicking on the elements.
    (Default sets to 'driver')
 
    airline_1 (str): The first airline to choose. 
    (Default sets to "Lufthansa")
    
    airline_2 (str): The second airline to choose. 
    (Default sets to "Qatar Airways")
 
    Return:
    -------
    None
    """
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
    # air_2 = driver.find_element(By.CSS_SELECTOR, "[data-testid='search_filter_airline_" + airline_2 + "']" )
    # air_2.click()


# In[10]:


def scrape_card(card_number: int = 0) -> dict:
    """
    Function that generates a dictionary of a specific flight-card (in this case round-trip ticket).

    Args:
    -----
        driver : The web driver to use for finding and clicking on the elements.
                        (Default sets to 'driver')
        
        card_number (int): number of flight card interested in
                        (Default sets to 0)

    Returns:
    --------
        dict: dictionnary of a specific flight-card

    Comments:
    ---------
        flight-cards: the offred results obtain when searching flight tickets. 
                        A flight-card includes relevant information of a flight-ticket.
        
        card_number: always starts at 0, 
                    i.e., the number of the first flight-card is 0.
        
        dictionnary: it contains 18 values which are,

            out_airline_company : name of the airline company for the outbound flight
            in_airline_company  : name of the airline company for the inbound flight
            dep_city            : departure city (where the flight starts form)
            arr_city            : arrival city (the destination of the flight)
            out_dep_date        : departure day of the outbound flight
            out_dep_time        : departure time of the outbound flight
            out_duration        : lenght (duration) of the outbound flight
            out_stop_number     : number of stopover(s) or layover(s)
            out_arr_date        : arrival day of the outbound flight
            out_arr_time        : arrival time of the outbound flight
            in_dep_date         : departure day of the inbound flight
            in_dep_time         : departure time of the inbound flight
            in_duration         : lenght of the inbound flight
            in_stop_num         : number of stopover(s) or layover(s)
            in_arr_date         : arrival day of the inbound flight
            in_arr_time         : arrival time of the inbound flight
            price_ticket        : flight price ticket

            hour_scrap          : hour in which the scrap has been done
            day_scrap           : day which the scrap has been performed
    """
    ticket = {}
    
    ticket['out_airline_company']= driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[3]/div/div/div'
        ).text
    
    ticket['in_airline_company']= driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[6]/div/div/div'
        ).text
    
    ticket['dep_city'] = driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]'
        ).text
    
    ticket['arr_city'] = driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]'
        ).text
    
    ticket['out_dep_date'] = driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[3]'
        ).text

    ticket['out_dep_time'] =  driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]'
        ).text
    
    ticket['out_duration'] = driver.find_element(
        By.XPATH, f"//*[@id='flight-card-{card_number}']/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]"
        ).text
    
    ticket['out_stop_num'] = driver.find_element(
        By.XPATH, f"//*[@id='flight-card-{card_number}']/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div[3]"
        ).text
    
    ticket['out_arr_date'] = driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div[3]'
        ).text
    
    ticket['out_arr_time'] = driver.find_element(
        By.XPATH, f"//*[@id='flight-card-{card_number}']/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div[1]"
        ).text
    
    ticket['in_dep_date'] = driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[4]/div[2]/div/div/div[1]/div[2]/div[3]'
        ).text
    
    ticket['in_dep_time'] = driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[4]/div[2]/div/div/div[1]/div[1]'
        ).text
    
    ticket['in_duration'] = driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[4]/div[2]/div/div/div[2]/div[1]'
        ).text
    
    ticket['in_stop_num'] = driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[4]/div[2]/div/div/div[2]/div[3]'
        ).text

    ticket['in_arr_date'] = driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[4]/div[2]/div/div/div[3]/div[2]/div[3]'
        ).text
    
    ticket['in_arr_time'] = driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[1]/div[4]/div[2]/div/div/div[3]/div[1]'
        ).text
    
    see_flight = driver.find_element(
        By.XPATH, f'//*[@id="flight-card-{card_number}"]/div/div/div[2]/div[2]/button'
    ).click()

    container = driver.find_elements(By.CSS_SELECTOR, ".SheetContainer-module__content___WX8xI")
    ticket['price_ticket'] = container[0].find_element(
        By.CSS_SELECTOR, ".css-vxcmzt"
        ).text
    driver.back()


    current_time = datetime.datetime.now()

    ticket['hour_scrap'] = current_time.hour
    ticket['day_scrap'] = current_time.day
    
    return(ticket)


# In[11]:


def scrape_cards(my_list: list = [])->list:
    """
    Function that generates list of dictionaries of n flight-card(s) for one search result page.

    Args:
    -----
        n_cards (int): n first flight-card(s)
        (Default sets to total number of flight-cards in one page)
    
    Returns:
    --------
        list: list of dictionnaries
    """
    n_cards = len(driver.find_elements(By.CSS_SELECTOR, ".css-4o3ibe"))

    for i in range(0, n_cards-1):
        my_list.append(scrape_card(i))

    return(my_list)


# In[12]:


list1 = []
list2 = []
def get_pages(list_pages: list = list1) -> list:
    """
    This function scrapes data from multiple pages by finding the total number of pages 
    and iterating through them. It scrapes the data from the cards on each page, sleeps for 2 seconds, 
    clicks on the next button, sleeps for 2 seconds, and scrapes the data from the cards on the next page.

    Args:
    -----
    driver : The web driver to use for finding and clicking on the elements.
    (Default sets to 'driver')

    my_list (list): The list to append the scraped data to.
    (Default sets to 'list1')
 
    Return:
    -------
    list: The list with the appended scraped data.
    """
    
    tot_pages = len(driver.find_elements(By.CSS_SELECTOR, '.Pagination-module__link___XUrx7, .Pagination-module__link___XUrx7:link, .Pagination-module__link___XUrx7:visited, .Pagination-module__separator___hRwOo'))
    for i in range(1, tot_pages+1):
        print(f"Scraping page {i}")
        next_button = driver.find_element(By.CSS_SELECTOR, f'button[aria-label=" {i}"]')
        next_button.click()
        scrape_cards(list_pages)
        time.sleep(3)
        # time.sleep(3)
    
    scrape_cards(list_pages)
    
    return(list_pages) 


# In[13]:


cur_time = datetime.datetime.now()
day = cur_time.day
hour = cur_time.strftime("%I")
hour_spe = cur_time.strftime("%p")

    
def convert_list(list1: list = list1, list2: list = list2):
    df1 = pd.DataFrame(list1)
    df2 = pd.DataFrame(list2)
    df = pd.concat([df1, df2], ignore_index=True)

    df.to_csv(f'booking_{day}_may_{hour}_{hour_spe}.csv', index=False)
    df.to_excel(f'booking_{day}_may_{hour}_{hour_spe}.xlsx', index=False)

    print("List has been successfully convert into excel and csv files")
    return(df)


# In[14]:


def export_files(name_folder : str = 'bxl_to_nyc'):
    shutil.move(f'booking_{day}_may_{hour}_{hour_spe}.csv', name_folder)
    shutil.move(f'booking_{day}_may_{hour}_{hour_spe}.xlsx', name_folder)

    print(f"The files have been exported to the right folder, i.e., {name_folder}")


# ## Data scraping of round flight from Bruxelles to New York City

# 1. Scrap data into list of dictionaries

# In[15]:


navigate_to_url()
manage_coockies()
go_to_flights()
input_from_city_airport()
input_to_city_airport()
round_trip_date_chooser()


# In[17]:


airline_chooser()


# In[18]:


list1 = get_pages()


# In[19]:


airline_chooser(airline_1 = "Swiss")
list2 = get_pages(list2)


# 2. Convert dataframe to CSV and Excel files

# In[20]:


convert_list()


# 3. Export files to the respective folder

# In[21]:


export_files()


# ## Data scraping of round flight from Bruxelles to São Paulo

# 1. Scrap data into list of dictionaries

# In[22]:


# navigate_to_url()
# manage_coockies()
go_to_flights()
input_from_city_airport()
input_to_city_airport(city="brazil", airport="AIRPORTGRU")
round_trip_date_chooser()


# In[24]:


airline_chooser()


# In[25]:


list3 = []
list4 = []
list3 = get_pages(list_pages = list3)


# In[26]:


airline_chooser(airline_1="Swiss")


# In[27]:


list4 = get_pages(list_pages=list4)


# In[28]:


driver.quit()


# 2. Convert dataframe to CSV and Excel files

# In[29]:


convert_list(list1= list3, list2=list4)


# 3. Export files to the respective folder

# In[30]:


export_files('bxl_to_sao')

