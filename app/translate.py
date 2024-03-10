from app.shared.utils import obtain_data
from transformers import pipeline
import logging
import tensorflow as tf

tf.get_logger().setLevel(logging.CRITICAL)


def __translate_es_to_en(message: str) -> str:
    pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")

    result = pipe(message)

    return result[0]["translation_text"]


def init_translate() -> None:
    try:
        data = obtain_data("Enter the data you want to translate")
    except Exception as e:
        print(e)
        return

    print(__translate_es_to_en(data))


if __name__ == "__main__":
    init_translate()
