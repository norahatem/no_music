FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y ffmpeg git && apt-get clean

RUN git clone https://github.com/norahatem/no_music.git

# CMD [ "python3", "no_music/main.py" ]