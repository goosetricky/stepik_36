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
selector = "input_value"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


b = browser.find_element_by_tag_name("#price")
WebDriverWait(browser, 15).until(
    expected_conditions.text_to_be_present_in_element((By.TAG_NAME, "#price"), "$100")
)
browser.find_element_by_tag_name("#book").click()
x_element = browser.find_element_by_id(selector)
x = x_element.text
print(x_element.text)
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_tag_name("button.btn").click()
#browser.find_element_by_id("solve").click()

time.sleep(101)
browser.quit()
