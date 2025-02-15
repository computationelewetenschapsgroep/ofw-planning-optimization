FROM python:3.9.6-slim-buster

RUN pip install --upgrade pip

WORKDIR /app
ENV WORKDIR /app
COPY pyproject.toml ./
# COPY poetry_install.py  ./

# RUN POETRY_HOME=/usr/local python3 poetry_install.py
# ENV POETRY="/usr/local/bin/poetry"
    

# RUN $POETRY config virtualenvs.create false \
#     && $POETRY install

RUN pip install fastapi=="0.112.1"
RUN pip install gunicorn=="23.0.0"
RUN pip install uvicorn=="0.30.6"
RUN pip install pydantic-settings=="2.3.4"
RUN pip install starlette=="0.38.2"

COPY . ./

ARG ADT_INSTANCE_NAME

ENV ADT_INSTANCE_NAME=${ADT_INSTANCE_NAME}

EXPOSE 8001


CMD env PATH=$PATH:$HOME/.local/bin $POETRY run ./run.sh
