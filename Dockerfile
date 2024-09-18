
# pull the official base image
FROM python:3.11.0b1-bullseye

# set work directory
WORKDIR /usr/src/app
COPY Pipfile /usr/src/app
COPY Pipfile.lock /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install jmespath
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --skip-lock --system --dev

# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000