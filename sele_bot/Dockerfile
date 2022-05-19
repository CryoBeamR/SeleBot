FROM python:3.8-slim

WORKDIR /app

COPY ./wait-for-grid.sh /app/wait-for-grid.sh
COPY ./requirements.txt /app/requirements.txt
COPY ./resources/Phantom.crx /app/Phantom.crx

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install jq -y\
    && apt-get install curl -y\
    && apt-get clean

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/
