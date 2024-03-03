import os
from dotenv import load_dotenv

from app.data.utility import QuickPass


def download_path() -> str:
	load_dotenv()
	return os.getenv("DOWNLOAD_PATH")


def get_personal_info() -> QuickPass:
	load_dotenv()
	data = QuickPass()
	data.url = os.getenv("SIGN_URL")
	data.ingress = os.getenv("INGRESS")
	data.legajo = os.getenv("LEGAJO")
	data.pin = os.getenv("PIN")

	return data
