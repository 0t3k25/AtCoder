FROM python:3.8-slim

RUN mkdir /app

WORKDIR /app

RUN apt-get update && apt-get install -y git \
libgl1-mesa-glx \
libglib2.0-0 \
libgtk2.0-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["bash"]