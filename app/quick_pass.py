from app.shared.environments import get_sign_quick_url, get_personal_info
from app.shared.web_driver import clickeable_button, text_field_send_keys, get_div_information, get_webdriver_data


def sign_in():
	data = get_webdriver_data(get_sign_quick_url())
	data_info = get_personal_info()

	clickeable_button(data.wait, "btnComenzar")

	text_field_send_keys(data.wait, "sensor_manual", data_info.ingress)

	clickeable_button(data.wait, "btnReiniciar")

	text_field_send_keys(data.wait, "legajo", data_info.legajo)

	text_field_send_keys(data.wait, "pin", data_info.pin)

	clickeable_button(data.wait, "btnFichar")

	information = get_div_information(data.driver, "divLog")

	data.driver.quit()
