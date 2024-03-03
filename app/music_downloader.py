from pytube import YouTube
from app.shared.environments import download_path
from app.shared.utils import obtain_download_data, rename_file


def datadownload():
	data = obtain_download_data("Enter url and file name")
	youtube = YouTube(data.url)
	try:
		video = youtube.streams.filter(only_audio=True).first()
		out_file = video.download(download_path())
		rename_file(out_file, f"{download_path()}/{data.name}")
	except:
		print("Something Went Wrong Please Try Again")
