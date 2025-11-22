from time import sleep

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 50
PROMISED_UP = 10
TWITTER_EMAIL = "gabpythontest@gmail.com"
TWITTER_PASSWORD= "pythontest1234"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver
        self.up=0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        go_button = driver.find_element(By.XPATH,
                                        value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')
        go_button.click()

        sleep(60)

        down_speed = driver.find_element(By.XPATH,
                                         value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"Down: {down_speed}")

        up_speed = driver.find_element(By.XPATH,
                                       value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Down: {up_speed}")


    def tweet_at_provider(self):
        self.driver.get("https://x.com/home")
        sleep(10)
        login = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        login.send_keys(TWITTER_EMAIL, Keys.ENTER)
        password = self.driver.find_element(By.XPATH,
                                            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

        sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()


bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()

