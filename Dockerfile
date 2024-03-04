FROM python:3.10-slim

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary


ADD . /code/