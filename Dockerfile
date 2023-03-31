FROM python:3.11-alpine3.16

COPY requirements.txt /temp/requirement.txt
COPY service /service
WORKDIR /service
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirement.txt

RUN adduser --disabled-password service-user

USER service-user


