import json
import pyperclip

from app.shared.utils import obtain_data


def format_json():
    try:
        data = obtain_data("Enter JSON as argument")
    except Exception as e:
        print(e)
        return e

    try:
        # Cargar el JSON y formatearlo
        json_obj = json.loads(data)
        json_formatted = json.dumps(json_obj, indent=2)

        pyperclip.copy(json_formatted)

    except ValueError as e:
        return "Error: JSON inválido - {}".format(e)


if __name__ == "__main__":
    format_json()
