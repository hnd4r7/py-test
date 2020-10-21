FROM python:3-alpine

MAINTAINER luli

RUN pip install -r requirements.txt

EXPOSE 80

CMD python app.py

