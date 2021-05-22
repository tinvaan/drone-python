FROM python:3.7-slim

RUN apt-get update && apt-get install -y build-essential python3-dev

RUN mkdir -p /drone-python
WORKDIR /drone-python
COPY . /drone-python

RUN pip install -r requirements.txt
ENV PYTHONPATH $(pwd):$PYTHONPATH
ENV DRONE_SERVER "https://cloud.drone.io"
