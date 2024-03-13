import pyshorteners

from app.shared.utils import data_on_clipboard, obtain_data


def shorten_url(url: str) -> None:
    shorter = pyshorteners.Shortener()
    shortened_url = shorter.tinyurl.short(url)
    data_on_clipboard(shortened_url)


def init_shortener() -> None:
    try:
        data = obtain_data("Enter a URL to shorten")
        shorten_url(data)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    init_shortener()
