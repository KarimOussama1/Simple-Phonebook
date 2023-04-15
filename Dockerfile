FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY . .
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt