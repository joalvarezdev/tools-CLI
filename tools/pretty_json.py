import json
import pyperclip

from tools.shared.utils import obtain_data


def format_json():
    data = obtain_data("Enter JSON as argument")
    try:
        # Cargar el JSON y formatearlo
        json_obj = json.loads(data)
        json_formatted = json.dumps(json_obj, indent=2)

        pyperclip.copy(json_formatted)

    except ValueError as e:
        return "Error: JSON inválido - {}".format(e)


format_json()
