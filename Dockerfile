FROM python:3.7

ENV PYTHONUNBUFFERED=1

RUN mkdir /opt/swapiback
WORKDIR /opt/swapiback

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000