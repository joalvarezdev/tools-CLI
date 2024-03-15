from app.utils.utils import obtain_data
from googletrans import Translator


def __translate_es_to_en(message: str) -> str:

    translator = Translator()

    result = translator.translate(message, dest="en").text

    return result


def init_translate() -> None:
    try:
        data = obtain_data("Enter the data you want to translate")
    except Exception as e:
        print(e)
        return

    print(__translate_es_to_en(data))


if __name__ == "__main__":
    init_translate()
