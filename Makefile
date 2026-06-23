# Makefile for Advent of Code
#
# This Makefile provides commands to set up the environment and run solutions for Advent of Code puzzles.
# It supports multiple languages (currently Python, Node.js, and Go).
#
# Targets:
# - setup: Sets up the environment for the specified language (default: Python).
#           Usage: make setup LANGUAGE=go
# - today: Runs the solution for today's puzzle (based on the current date).
#           Usage: make today LANGUAGE=go
# - aoc: Runs the solution for a specific puzzle by year and day.
#         Usage: make aoc LANGUAGE=go YEAR=2025 DAY=1
#
# Variables:
# - LANGUAGE: Specifies the programming language to use (python, js, or go). Default: python.
# - YEAR: Specifies the year of the puzzle (default: 2015).
# - DAY: Specifies the day of the puzzle (default: 1).
#
# Example:
#   make setup LANGUAGE=go
#   make today LANGUAGE=go
#   make aoc LANGUAGE=go YEAR=2025 DAY=1
SHELL := /bin/zsh

PYTHON_VERSION = 3.13
PYTHON_ENV_NAME = adventofcode
NPM_VERSION = 22
GO_VERSION = 1.23

.PHONY: setup today aoc

# Select language: python, js, or go
LANGUAGE ?= python

# Load environment based on the selected language
setup:
	@source ~/.zshrc; \
	if [ "$(LANGUAGE)" = "python" ]; then \
		echo "Setting up Python"; \
		pyenv virtualenv --force $(PYTHON_VERSION) $(PYTHON_ENV_NAME); \
		echo "$(PYTHON_ENV_NAME)" > .python-version; \
		eval "$$(pyenv init -)" && pyenv activate ${PYTHON_ENV_NAME}; \
		pip install -r requirements.txt; \
	elif [ "$(LANGUAGE)" = "js" ]; then \
		echo "Setting up Node.js"; \
		nvm install $(NPM_VERSION); \
		nvm use $(NPM_VERSION); \
		npm install; \
		echo "Setting up Python as well, sorry but you needed it for the aoc_helper"; \
		pyenv virtualenv --force $(PYTHON_VERSION) $(PYTHON_ENV_NAME); \
		echo "$(PYTHON_ENV_NAME)" > .python-version; \
		eval "$$(pyenv init -)" && pyenv activate ${PYTHON_ENV_NAME}; \
		pip install -r requirements.txt; \
	elif [ "$(LANGUAGE)" = "go" ]; then \
		echo "Setting up Go"; \
		eval "$$(brew shellenv)"; \
		brew install go@$(GO_VERSION); \
		echo "Go $(GO_VERSION) installed successfully"; \
	else \
		echo "Unsupported language: $(LANGUAGE)"; \
		exit 1; \
	fi

# Run the script for today's puzzle if it's December
# Supports Python, Node.js, and Go
# Usage: make today LANGUAGE=go
# Default: LANGUAGE=python
today:
	@source ~/.zshrc; \
	if [ "$(LANGUAGE)" = "python" ]; then \
		echo "Running AoC Python script for today..."; \
		eval "$$(pyenv init -)" && pyenv activate ${PYTHON_ENV_NAME}; \
		python support/aoc_helper.py --year "$$(date '+%Y')" --day "$$(date '+%d')"; \
	elif [ "$(LANGUAGE)" = "js" ]; then \
		echo "Running AoC Node.js script for today..."; \
		nvm use $(NPM_VERSION); \
		node support/aoc_helper.js --year "$$(date '+%Y')" --day "$$(date '+%d')"; \
	elif [ "$(LANGUAGE)" = "go" ]; then \
		echo "Running AoC Go script for today..."; \
		eval "$$(pyenv init -)" && pyenv activate ${PYTHON_ENV_NAME}; \
		python support/aoc_helper.py --year "$$(date '+%Y')" --day "$$(date '+%d')" --language go; \
	else \
		echo "Unsupported language: $(LANGUAGE)"; \
		exit 1; \
	fi

# Run the script for a specific puzzle by year and day
# Supports Python, Node.js, and Go
# Usage: make aoc LANGUAGE=go YEAR=2025 DAY=1
# Default: LANGUAGE=python, YEAR=2015, DAY=1
aoc:
	@source ~/.zshrc; \
	if [ "$(LANGUAGE)" = "python" ]; then \
		echo "Running Python AoC..."; \
		eval "$$(pyenv init -)" && pyenv activate ${PYTHON_ENV_NAME}; \
		python support/aoc_helper.py --year $(YEAR) --day $(DAY); \
	elif [ "$(LANGUAGE)" = "js" ]; then \
		echo "Running Node.js AoC..."; \
		nvm use $(NPM_VERSION); \
		eval "$$(pyenv init -)" && pyenv activate ${PYTHON_ENV_NAME}; \
		python support/aoc_helper.py --year $(YEAR) --day $(DAY) --language js; \
	elif [ "$(LANGUAGE)" = "go" ]; then \
		echo "Running Go AoC..."; \
		eval "$$(pyenv init -)" && pyenv activate ${PYTHON_ENV_NAME}; \
		python support/aoc_helper.py --year $(YEAR) --day $(DAY) --language go; \
	else \
		echo "Unsupported language: $(LANGUAGE)"; \
		exit 1; \
	fi
