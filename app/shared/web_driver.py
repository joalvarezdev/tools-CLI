from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

from app.data.dto import WebDriverObj


def clickeable_button(web_driver: WebDriverWait, html_id_element: str):
	button = web_driver.until(ec.element_to_be_clickable((By.ID, html_id_element)))
	button.click()


def text_field_send_keys(web_driver: WebDriverWait, html_id_element: str, send_info: str):
	text_field = web_driver.until(ec.visibility_of_element_located((By.ID, html_id_element)))
	text_field.send_keys(send_info)


def get_div_information(test: WebDriver, html_id_element: str) -> str:
	time.sleep(3)
	return test.find_element(By.ID, html_id_element).text


def get_webdriver_data(url_open: str) -> WebDriverObj:
	driver = webdriver.Chrome()
	driver.get(url_open)

	data = WebDriverObj()
	data.wait = WebDriverWait(driver, 10)
	data.driver = driver

	return data
