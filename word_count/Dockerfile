FROM python:3.11

RUN apt-get update && apt-get upgrade -y

WORKDIR /app

RUN pip install poetry
COPY pyproject.toml ./
COPY app app
COPY tests tests

RUN poetry install
RUN poetry run pip install pydantic[dotenv]

CMD ["poetry", "run", "app"]
