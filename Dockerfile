FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING=UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV TZ=Europe/Kiev

RUN mkdir /pjbook
WORKDIR /pjbook

COPY . /pjbook

RUN pip install -r requirements.txt