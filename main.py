import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
import math
from selenium.webdriver.support.ui import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome("C:/chromedriver.exe")
browser.get(link)
selector = "input_vaaluse"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


print(True)
time.sleep(101)
browser.quit()
