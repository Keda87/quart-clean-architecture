FROM python:3.7.2-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/app/code
WORKDIR /usr/app/code

RUN apk add postgresql-dev \
    && apk add build-base gcc abuild binutils binutils-doc gcc-doc \
    && rm -rf /var/cache/apk/*

COPY . /usr/app/code

RUN pip install -r requirements.txt