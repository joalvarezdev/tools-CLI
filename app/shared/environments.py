import os
from dotenv import load_dotenv


def download_path() -> str:
	load_dotenv()
	return os.getenv("DOWNLOAD_PATH")
