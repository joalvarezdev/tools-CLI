from app.shared.environments import get_personal_info
from app.shared.web_driver import clickeable_button, text_field_send_keys, get_div_information, get_webdriver_data
from app.shared.utils import obtain_data_default
from app.shared.quick_file_utils import save_registry


def __sign_in_quick_pass():
	data_info = get_personal_info()
	data = get_webdriver_data(data_info.url)

	clickeable_button(data.wait, "btnComenzar")

	text_field_send_keys(data.wait, "sensor_manual", data_info.ingress)

	clickeable_button(data.wait, "btnReiniciar")

	text_field_send_keys(data.wait, "legajo", data_info.legajo)

	text_field_send_keys(data.wait, "pin", data_info.pin)

	clickeable_button(data.wait, "btnFichar")

	status = get_div_information(data.driver, "divLog")
	print(status)
	save_registry(status)

	data.driver.quit()


def sign_in():
	data = obtain_data_default()
	if not data:
		__sign_in_quick_pass()
	else:
		save_registry("Ingreso correcto")
