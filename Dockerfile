FROM python:3.8.12-slim-buster

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

CMD FLASK_DEBUG=1 FLASK_APP=./servers/app.py flask run -h 0.0.0.0;
