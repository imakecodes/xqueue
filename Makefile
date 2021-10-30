all: help

help:
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"
	@echo "ℹ️ Available commands ℹ️"
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"
	@echo "⭐️ help               : Shows this message"
	@echo "⭐️ local-run          : Runs the application locally"
	@echo "⭐️ dev-setup          : Prepares the local dev setup"
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"

local-run:
	@uvicorn app.main:app --host 0.0.0.0 --port 8008 --reload

dev-setup:
	@pip install -r requirements.txt
	@pip install -r requirements-dev.txt
	@pre-commit install
