from time import sleep

import ec
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

FB_USERNAME= "gabrielaweya"
FB_pass = "londonchelsea"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

# wait = WebDriverWait(driver,2)

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(2)

fb_button = driver.find_element(By.XPATH, value='//*[@id="q1685428402"]/div/div/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button')
fb_button.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

sleep(4)

fb_email = driver.find_element(By.NAME, value= "email")
fb_email.send_keys(FB_USERNAME)

fb_password = driver.find_element(By.NAME, value= "pass")
fb_password.send_keys(FB_pass, Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)

allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()