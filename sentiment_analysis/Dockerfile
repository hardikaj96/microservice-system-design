FROM python:3.11

RUN apt-get update && apt-get upgrade -y

WORKDIR /app

RUN python3.11 -m ensurepip && pip install -U pip && pip install poetry
COPY pyproject.toml ./
COPY app app
COPY tests tests

RUN poetry install
RUN poetry run pip install pydantic[dotenv]

RUN poetry run python -m nltk.downloader vader_lexicon

CMD ["poetry", "run", "app"]
