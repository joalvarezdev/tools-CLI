#!/usr/bin/bash

poetry run black .
poetry run flake8 --exclude=.venv --max-line-length=88
