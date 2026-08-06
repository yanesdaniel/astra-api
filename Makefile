.PHONY: help pip-install uv-install run check check-fix format test

help:
	@echo "====================================================================="
	@echo "                      Astra API Commands                             "
	@echo "====================================================================="
	@echo "  help        - Shows this help menu"
	@echo "  pip-install - Installs dependencies using pip from requirements.txt"
	@echo "  uv-install  - Syncs and installs dependencies using uv"
	@echo "  run         - Starts the development server at main.py"
	@echo "  check       - Analyses the code for errors using ruff"
	@echo "  check-fix   - Analyses and automatically fixes errors using ruff"
	@echo "  format      - Applies automatic formatting to the code using ruff"
	@echo "  test        - Runs tests with pytest"
	@echo "====================================================================="

pip-install:
	pip install -r requirements.txt

uv-install:
	uv sync

run:
	python main.py

check:
	ruff check

check-fix:
	ruff check --fix

format:
	ruff format

test:
	pytest tests/ -v