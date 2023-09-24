FROM python:latest
LABEL authors="ismarhahazov"
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
WORKDIR /DRFTELBOT1

COPY requirements.txt /DRFTELBOT1/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . .