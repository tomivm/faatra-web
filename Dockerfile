FROM python:3.8

RUN python -m pip install --upgrade pip

COPY pyproject.toml pyproject.toml

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev 

COPY faatra/ .