from pytube import YouTube
from app.shared.environments import download_path
from app.shared.utils import obtain_download_data, rename_file
from app.shared.file_utils import remove_file

import subprocess


def __data_download():
    data = obtain_download_data("Enter url and file name")
    youtube = YouTube(data.url)
    try:
        video = youtube.streams.filter(only_audio=True).first()
        out_file = video.download(download_path())
        file_name = f"{download_path()}/{data.name}"

        rename_file(out_file, file_name)

        video = f"{file_name}.mp4"

        __convert_video_to_mp3(video, f"{file_name}.mp3")

        remove_file(video)

    except Exception as e:
        print("Something Went Wrong Please Try Again")
        print(e)


def __convert_video_to_mp3(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i",
        input_file,
        "-vn",
        "-acodec",
        "libmp3lame",
        "-ab",
        "192k",
        "-ar",
        "44100",
        "-y",
        output_file,
    ]

    try:
        subprocess.run(
            ffmpeg_cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.DEVNULL,
        )
        print("Success")
    except subprocess.CalledProcessError as e:
        print("Conversion failed!")
        print(e)


if __name__ == "__main__":
    __data_download()
