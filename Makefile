PYTHON_VERSION = 3.13
PYTHON_ENV_NAME = adventofcode

.PHONY: setup today aoc

# Load Python virtual environment
setup:
	# pyenv install $(PYTHON_VERSION)
	pyenv virtualenv --force $(PYTHON_VERSION) $(PYTHON_ENV_NAME)
	echo "$(PYTHON_ENV_NAME)" > .python-version
	@eval "$$(pyenv init -)" && pyenv activate ${PYTHON_ENV_NAME}
	pip install -r requirements.txt
	echo "Python environment $(PYTHON_ENV_NAME) set up and dependencies installed."

# Run the script for today's puzzle if it's December
today:
	@eval "$$(pyenv init -)" && pyenv activate ${PYTHON_ENV_NAME}
	@puzzle_path=$$(python support/aoc_helper.py --year $$(date '+%Y') --day $$(date '+%d') | tail -n 1); \
	cd "$$puzzle_path" && code main.py

# Run the script for a specific puzzle by year and day
# Usage: make aoc YEAR=2024 DAY=5
YEAR ?= 2015
DAY ?= 1
aoc:
	@eval "$$(pyenv init -)" && pyenv activate ${PYTHON_ENV_NAME}
	@puzzle_path=$$(python support/aoc_helper.py --year $$YEAR --day $$DAY | tail -n 1); \
	cd "$$puzzle_path" && code main.py
