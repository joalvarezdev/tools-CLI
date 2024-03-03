import base64
import pyperclip

from app.shared.utils import obtain_data


def base_64_encode():
    data = obtain_data("Insert a valid data")
    encoded_data = base64.b64encode(data.encode())
    pyperclip.copy(str(encoded_data))
