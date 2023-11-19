POETRY_RUN_CMD := poetry run
DOCKER_COMPOSE_CMD := docker compose
DOCKER_COMPOSE_RUN_MAIN := docker compose run app
DOCKER_COMPOSE_RUN_SENTIMENT_ANALYSIS := docker compose run sentiment_analysis
DOCKER_COMPOSE_RUN_WORD_COUNT := docker compose run word_count
DOCKER_COMPOSE_RUN_ENTITY_RECOGNITION := docker compose run entity_recognition

default: help

.SILENT: help 

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done


.PHONY: test
test: # 🧪 Run tests in poetry shell
	cd ./tests && poetry shell && poetry install && pytest && poetry env remove



.PHONY: test-services
test-services: # 🧪 Run tests in services container
	$(DOCKER_COMPOSE_RUN_MAIN) $(POETRY_RUN_CMD) pytest --cov=app --cov-report term-missing && $(DOCKER_COMPOSE_RUN_SENTIMENT_ANALYSIS) $(POETRY_RUN_CMD) pytest --cov=app --cov-report term-missing && $(DOCKER_COMPOSE_RUN_WORD_COUNT) $(POETRY_RUN_CMD) pytest --cov=app --cov-report term-missing && $(DOCKER_COMPOSE_RUN_ENTITY_RECOGNITION) $(POETRY_RUN_CMD) pytest --cov=app --cov-report term-missing


.PHONY: shell 
shell: # get a bash shell in the main service container 
	$(DOCKER_COMPOSE_RUN_MAIN) bash 


.PHONY: test-verbose
test-verbose: # 🧪 Run tests with verbose output (pytest -s)
		$(DOCKER_COMPOSE_RUN_MAIN) $(POETRY_RUN_CMD) pytest --cov=app --cov-report term-missing -s && $(DOCKER_COMPOSE_RUN_SENTIMENT_ANALYSIS) $(POETRY_RUN_CMD) pytest --cov=app --cov-report term-missing -s && $(DOCKER_COMPOSE_RUN_WORD_COUNT) $(POETRY_RUN_CMD) pytest --cov=app --cov-report term-missing -s && $(DOCKER_COMPOSE_RUN_ENTITY_RECOGNITION) $(POETRY_RUN_CMD) pytest --cov=app --cov-report term-missing -s

.PHONY: logs 
logs: # Start the API server in docker
	$(DOCKER_COMPOSE_CMD) logs -f


.PHONY: docker compose up
up: # ⭐ Run checks that should run successfully before creating a pull request
	$(DOCKER_COMPOSE_CMD) up -d


.PHONY: down 
down: # docker compose down 
	$(DOCKER_COMPOSE_CMD) down 


.PHONY: build
build: # docker compose build
	$(DOCKER_COMPOSE_CMD) build


.PHONY: build-no-cache
build-no-cache: # docker compose build --no-cache
	$(DOCKER_COMPOSE_CMD) build --no-cache
