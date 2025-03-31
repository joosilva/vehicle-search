PYTHON = python3
PIP = pip
DOCKER = docker
CONTAINER_NAME = vehicle-search-container

install:
	$(PIP) install --no-cache-dir -r requirements.txt

test:
	$(PYTHON) -m pytest

build:
	$(DOCKER) build -t vehicle-search .

run:
	$(DOCKER) run -it --rm --name $(CONTAINER_NAME) vehicle-search

run-dev:
	$(DOCKER) run -it --rm -p 5000:5000 --name $(CONTAINER_NAME) vehicle-search

test-docker:
	$(DOCKER) run --rm vehicle-search pytest

clean:
	$(DOCKER) system prune -f

stop:
	$(DOCKER) stop $(CONTAINER_NAME) || true
