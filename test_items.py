import pytest
import time
import math
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# функция, определяющая наличие элемента на странице
def is_exist_element(browser, selector_xpath):
    try:
        browser.find_element(By.XPATH, selector_xpath)
        return True
    except:
        return False


class TestMain:
    def test_exist_add_button(self, browser):
        # Ссылка на сайт
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        # переходим на сайт
        browser.get(link)

        # определяем есть ли кнопка
        assert is_exist_element(browser, "//form[@id='add_to_basket_form']//button"), "Кнопки нет на странице"

        # Для проверки французской версии
        # time.sleep(30)
