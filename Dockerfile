FROM python:3.9.19-slim

WORKDIR /app
COPY requirements.txt ./
EXPOSE 8000

RUN pip install -r requirements.txt

RUN adduser --disabled-password service-user

USER service-user
