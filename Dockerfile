FROM python:3.11-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y libpq-dev gcc


COPY ./requirements ./requirements
COPY ./scripts ./scripts
RUN pip install --upgrade pip && pip install pip-tools && \
    pip-compile requirements/requirements.in && \
    pip-sync requirements/requirements.txt && \
    chmod +x ./scripts/docker-entrypoint.sh && \
    chmod 755 ./scripts/docker-entrypoint.sh

COPY . .

ENTRYPOINT ["sh", "/usr/src/app/scripts/docker-entrypoint.sh"]
