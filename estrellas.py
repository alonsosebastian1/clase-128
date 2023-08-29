from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time 
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser=webdriver.Chrome("C://Users//alons//Desktop//Byjus//PRO_C128_AM2_V1-main//chromedriver_win32//chromedriver.exe")
browser.get(START_URL)

time.sleep(100)
scraped_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table = soup.find("table", attrs={"class","wikitable"})

    table_body = bright_star_table.find("tbody")

    table_rows = table_body.find_all("tr")

    for row in table_rows:
        table_cols = row.find_all("td")
        #print(table_cols)
        temp_list = []


        for col_data in table_cols:
            data = col_data.text.strip()
            print(col_data.text)
    