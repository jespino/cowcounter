FROM python:3.4

RUN pip install django==1.8 gunicorn

COPY cowcounter /app/cowcounter
COPY cows /app/cows
COPY manage.py /app/

ENTRYPOINT gunicorn --chdir /app cowcounter.wsgi:application
