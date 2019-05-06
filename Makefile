help:
	@echo ""
	@echo "  deps       to install the required files for development"
	@echo "  build      to install the client CLI application"
	@echo "  up         to run the entire application via docker-compose"
	@echo "  down       to stop the application via docker-compose"
	@echo "  run        to run the server application via Flask natively (without docker-compose)"
	@echo "  test       to run all tests"
	@echo ""


.PHONY: build
build: test package

.PHONY: deps
deps:
	pip install -q -r requirements_dev.txt

.PHONY: package
package:
	pip install -e .

.PHONY: up
up:
	docker-compose up --build

.PHONY: down
down:
	docker-compose down

.PHONY: run
run:
	./local_run.sh

.PHONY: clean
clean: down
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -iname '*__pycache__*' -exec rm -rf {} +
	coverage erase

.PHONY: test
test: deps
	flake8
	pydocstyle
	coverage erase
	nosetests --with-coverage --cover-package=server
	nosetests --with-coverage --cover-package=client
	coverage report --fail-under 100 server/*.py client/*.py
	./run_pact.sh
