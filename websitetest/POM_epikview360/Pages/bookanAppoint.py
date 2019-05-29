from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import HtmlTestRunner
import unittest
# import urllib3
# import re
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://epikview360.com/booking/")
driver.maximize_window()
# time.sleep(20)
driver.implicitly_wait(30)
time.sleep(5)
frame = driver.find_element_by_tag_name('iframe')



