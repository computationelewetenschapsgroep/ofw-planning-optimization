FROM python:3.9.6-slim-buster

RUN pip install --upgrade pip

WORKDIR /app
ENV WORKDIR /app
COPY pyproject.toml ./
COPY poetry_install.py  ./

RUN POETRY_HOME=/usr/local python3 poetry_install.py
ENV POETRY="/usr/local/bin/poetry"
    

RUN $POETRY config virtualenvs.create false \
    && $POETRY install

COPY . ./

ARG ADT_INSTANCE_NAME

ENV ADT_INSTANCE_NAME=${ADT_INSTANCE_NAME}

EXPOSE 8001


CMD env PATH=$PATH:$HOME/.local/bin $POETRY run ./run.sh
