import json
import os

from app.utils.utils import get_current_date
from app.utils.environments import get_root_dir_quick

ROOT_DIR = get_root_dir_quick()
LOGS_DIR = f"{ROOT_DIR}/logs"
SUCCESS_SIGN = ["Ingreso", "correcto"]


def __verify_and_create_dir(path: str):
    if not os.path.exists(path):
        os.mkdir(path)


def __get_current_registry():
    return {
        "day": f"{get_current_date('%d')}-{get_current_date('%a')}",
        "time": get_current_date("%H:%M:%S"),
    }


def __verify_dir_structure() -> str:
    __verify_and_create_dir(LOGS_DIR)
    current_year_path = f"{LOGS_DIR}/{get_current_date('%Y')}"
    __verify_and_create_dir(current_year_path)
    return f"{current_year_path}/{get_current_date('%b')}.json"


def __json_write_value(path: str, registry: str):
    with open(path, "w") as file:
        json.dump(registry, file, indent=2)


def __json_load_data(path: str):
    with open(path, "r") as file:
        return json.load(file)


def save_registry(status: str):
    if all(word in status for word in SUCCESS_SIGN):
        current_month_file = __verify_dir_structure()
        if not os.path.isfile(current_month_file):
            __json_write_value(current_month_file, [__get_current_registry()])
        else:
            content = __json_load_data(current_month_file)

            content.append(__get_current_registry())

            __json_write_value(current_month_file, content)
