VENV ?= venv
REQUIREMENTS ?= requirements-dev.txt
COV_REPORT := html

init: clean init-venv init-precommit

init-venv: clean-venv create-venv update-venv
	@echo ""
	@echo "Do not forget to activate your new virtual environment"

create-venv:
	@echo "Creating virtual environment: $(VENV)..."
	@python3 -m venv $(VENV)

update-venv:
	@echo "Updating virtual environment: $(VENV)..."
	@( \
		. $(VENV)/bin/activate; \
		pip install --upgrade pip; \
		pip install -r $(REQUIREMENTS) \
	)

init-precommit:
	@echo "Installing pre commit..."
	@( \
		. $(VENV)/bin/activate; \
		pre-commit install; \
	)

clean: clean-pyc clean-test clean-venv


clean-venv:
	@echo "Removing virtual environment: $(VENV)..."
	@rm -rf $(VENV)

clean-test: clean-pyc
	@echo "Removing previous test data..."
	@rm -rf .coverage
	@rm -rf htmlcov
	@rm -rf test-reports
	@rm -f coverage.xml
	@rm -rf .pytest_cache


clean-pyc:
	@echo "Removing compiled bytecode files..."
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +


unit-test: clean-test unit-pytest

unit-pytest:
	@echo "Running test..."
	@( \
		. $(VENV)/bin/activate; \
		pytest --log-cli-level=WARN; \
	)

coverage: clean-test coverage-pytest

coverage-pytest:
	@echo "Running test with coverage report..."
	@( \
		. $(VENV)/bin/activate; \
		pytest \
			--cov=servers \
			--cov-report $(COV_REPORT) \
			--no-cov-on-fail; \
	)

integration-test: clean-test integration-pytest

integration-pytest:
	@echo "Running component tests..."
	@( \
		. $(VENV)/bin/activate; \
		pytest integration --log-cli-level=WARN; \
	)

service-run:
	@echo "Starting server"
