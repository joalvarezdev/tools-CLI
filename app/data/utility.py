from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class DownloadData:
	url: str
	name: str


class WebDriverObj:
	driver: WebDriver
	wait: WebDriverWait


class QuickPass:
	ingress: str
	legajo: str
	pin: str
