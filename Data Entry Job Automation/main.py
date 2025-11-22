import re
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By

url = "https://docs.google.com/forms/d/e/1FAIpQLSf5X_dNsyBY3TIxnjXoXNjuzjR_QnHHFcZhGQh_GNSA40Tj9g/viewform?usp=header"


response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
zillow = response.text

soup = BeautifulSoup(zillow,"html.parser")
listings = soup.find_all(name= "a", class_ = "StyledPropertyCardDataArea-anchor")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True )

driver = webdriver.Chrome(options=chrome_options)





listings_url = []
for a in listings:
    li = a.get("href")
    listings_url.append(li)

price = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")


prices = []
for b in price:
    li=b.getText()
    prices.append(li)

price_list =[]
for  c in prices:
    clean = c.split('+')[0].split('/')[0].strip()
    price_list.append(clean)


loc= soup.find_all(name="address")

locations=[]
for d in loc:
    nn = d.getText()
    locations.append(nn)
locations_list = []
for e in locations:
    aa = e.strip().replace('\n', '').replace('  ', ' ')
    locations_list.append(aa)



for i in range (0,len(listings_url)):
    driver.get(url)

    sleep(2)
    address_input = driver.find_element(By.XPATH,  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(locations_list[i])

    sleep(1)

    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price_list[i])

    sleep(1)

    url_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url_input.send_keys(listings_url[i])

    sleep(1)

    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()


    sleep(3)



print(price_list)
print(locations_list)

#     bi = b.getText()
#     price_list.append(bi)




print(listings_url)



url = "https://docs.google.com/forms/d/e/1FAIpQLSf5X_dNsyBY3TIxnjXoXNjuzjR_QnHHFcZhGQh_GNSA40Tj9g/viewform?usp=header"