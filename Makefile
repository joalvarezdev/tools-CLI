include .env

SHELL = /bin/bash
ROOT_DIR = $(shell pwd)
SCRIPT_DIR = $(ROOT_DIR)/provision/scripts

GIT_INIT = $(SHELL) $(SCRIPT_DIR)/git-init.sh
PRE_COMMIT_CONFIG = $(SHELL) $(SCRIPT_DIR)/pre-commit-config.sh
LINTERS = $(SHELL) $(SCRIPT_DIR)/linters.sh

configure:
	@$(GIT_INIT)
	@$(PRE_COMMIT_CONFIG)

build:
	@poetry update

lint:
	@$(LINTERS)

init:
	@poetry shell
