FROM python:3.9-slim

RUN mkdir /app
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
RUN true

COPY . /app
