FROM python:2.7

ADD requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install --proxy 40.0.40.10:9000 --upgrade pip
RUN pip install --proxy 40.0.40.10:9000 -r requirements.txt
RUN adduser --disabled-password --gecos '' myuser
