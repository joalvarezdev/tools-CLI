#!/usr/bin/bash

poetry install &> /dev/null

source ./.venv/bin/activate

pre-commit install
