FROM ubuntu:latest

RUN apt-get update

WORKDIR /stegoServer

COPY server.py server.py
COPY client.py client.py
COPY db.py db.py
COPY mail.py mail.py
COPY encrypt.py encrypt.py
COPY steg_image_LSB.py steg_image_LSB.py
COPY steg_audio.py steg_audio.py
