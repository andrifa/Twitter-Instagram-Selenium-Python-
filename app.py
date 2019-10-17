import os
import sys
import codecs
import pprint
import time

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait

class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login")
        time.sleep(3)
        email = bot.find_element_by_class_name("js-username-field")
        password = bot.find_element_by_class_name("js-password-field")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get("https://twitter.com/search?q="+hashtag+"&src=typed_query")
        time.sleep(3)
        for _ in range (1,3):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            tweets = bot.find_elements_by_class_name("r-3s2u2q")
            links = [elem.get_attribute("href")
                    for elem in tweets]
            for link in links:
                if link == None:
                    pass
                else:
                    bot.get(link)
                    # try:
                    like=bot.find_element_by_class_name("css-901oao")

                    # div = bot.find_elements_by_class_name("css-18t94o4")
                    # print(div)
                    # coba = [klik.get_attribute("data-testid") for klik in div]
                    # print(coba)                        
                    # # klik.click()

                    time.sleep(10)
                    # except Exception as ex:
                    #     time.sleep(10)

ed = TwitterBot("afauzanadziima@gmail.com","2354ndry")
ed.login()
ed.like_tweet('webdevelopment')
    


# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# class PythonOrgSearch(unittest.TestCase):

#  def setUp(self):
#   self.driver = webdriver.Firefox()

#  def test_search_in_python_org(self):
#   driver = self.driver
#   driver.get("https://twitter.com/login")

#   driver.maximize_window()
  
#   username = driver.find_element_by_class_name("js-username-field")
#   password = driver.find_element_by_class_name("js-password-field")

#   username.send_keys("afauzanadziima@gmail.com")
#   password.send_keys("2354ndry")
#   password.send_keys(Keys.RETURN)

#   wait = ui.WebDriverWait(driver, 5)
#   driver.find_element_by_css_selector("submit").click()


#  def tearDown(self):
#   #self.driver.close()
#   print ("close?")

# if __name__ == "__main__":
#  unittest.main()

