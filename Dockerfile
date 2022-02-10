FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SECRET_KEY dnm2q12rr9pgnrvwb$h+t9#y72(!b4fws&y)vmd!-+t+f5@#wc
RUN mkdir /webapps
WORKDIR /webapps
RUN apt-get update && apt-get upgrade -y && apt-get install -y 
RUN pip install -U pip setuptools

COPY requirements.txt /webapps/
RUN pip install -r /webapps/requirements.txt

ADD . /webapps/

EXPOSE 8000