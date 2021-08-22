FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install mysql-connector-python
RUN pip3 install opencv-python

WORKDIR /stegoServer

COPY server.py server.py
COPY client.py client.py

RUN mkdir scripts
RUN mkdir server_files

COPY scripts scripts/
COPY server_data server_data/
