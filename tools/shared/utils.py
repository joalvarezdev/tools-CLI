import sys


def obtain_data(message: str):
    if len(sys.argv) < 2:
        print(message)
    else:
        return sys.argv[1]
