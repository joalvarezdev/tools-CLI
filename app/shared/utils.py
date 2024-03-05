import os
import sys
import time

from app.data.dto import DownloadData


def obtain_data(message: str):
	if len(sys.argv) < 2:
		print(message)
	else:
		return sys.argv[1]


def obtain_data_default() -> str:
	if len(sys.argv) < 2:
		return ""
	else:
		return sys.argv[1]


def obtain_download_data(message: str) -> DownloadData:
	if len(sys.argv) < 3:
		print(message)
	else:
		data = DownloadData()
		data.url = sys.argv[1]
		data.name = sys.argv[2]
		return data


def rename_file(out_file: str, name: str):
	base, ext = os.path.splitext(out_file)
	new_file = name + ext
	os.rename(out_file, new_file)


def get_current_date(data_obtain: str) -> str:
	return time.strftime(data_obtain)
