from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

SIMILAR_ACCOUNT = "rolex"
USERNAME="gabpythontest"
PASSWORD= 'Coolsteeze1'






class Instafollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)




    def login(self):
        self.driver.get("https://www.instagram.com")
        sleep(3)
        email = self.driver.find_element(By.NAME, value="username")
        email.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, value='password')
        password.send_keys(PASSWORD, Keys.ENTER)

    def find_follwers(self):
        sleep(5)
        self.driver.get("https://www.instagram.com/rolex/followers/")
        sleep(5)
        # x_path ='/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]'
        # modal= self.driver.find_element(By.XPATH, value= x_path)
        # for i in range(10):
        #     # In this case we're executing some Javascript, that's what the execute_script() method does.
        #     # The method can accept the script as well as an HTML element.
        #     # The modal in this case, becomes the arguments[0] in the script.
        #     # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     sleep(2)
    def follow(self):
        button = self.driver.find_elements(By.CSS_SELECTOR, value='._anno button')
        for button in button:
            button.click()
            sleep(1)
            button.click()
            sleep(1)





bot = Instafollower()
bot.login()
bot.find_follwers()
bot.follow()