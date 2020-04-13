FROM python:3
ENV PYTHONUNBUFFERED 1
RUN set -x \
    && apt-get update \
    && apt-get upgrade
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD python3 manage.py runserver 0.0.0.0:8000
