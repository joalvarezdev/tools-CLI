import uuid
import pyperclip


def uuid_generator():
    pyperclip.copy(str(uuid.uuid4()))
