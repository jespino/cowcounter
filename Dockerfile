FROM python:3.4

COPY cowcounter /app/cowcounter
COPY cows /app/cows
COPY manage.py /app/
RUN pip install django==1.8 gunicorn

APP gunicorn cowcounter.wsgi:application
