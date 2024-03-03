#include .env


SHELL = /bin/bash
ROOT_DIR = $(shell pwd)
SCRIPT_DIR = $(ROOT_DIR)/provision/scripts

PRE_COMMIT_CONFIG = $(SHELL) $(SCRIPT_DIR)/pre-commit-config.sh

precommit:
	@$(PRE_COMMIT_CONFIG)

build:
	@poetry install
