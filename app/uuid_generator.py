import uuid
import pyperclip


def uuid_generator():
    pyperclip.copy(str(uuid.uuid4()))


if __name__ == "__main__":
    uuid_generator()
