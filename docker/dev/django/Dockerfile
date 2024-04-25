FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y gcc python3-dev musl-dev libmagic1 libffi-dev netcat-traditional sqlite3 \
    build-essential libpq-dev 

COPY poetry.lock pyproject.toml /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY ./docker/dev/django/entrypoint /entrypoint

RUN chmod +x /entrypoint

COPY . /app/

ENTRYPOINT [ "/entrypoint" ]