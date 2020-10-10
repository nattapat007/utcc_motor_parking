# Pull base image
FROM python:3.8-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /code
WORKDIR /code

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev

# Install dependencies
COPY requirements.txt /code//requirements.txt
RUN pip install pip && pip install -r requirements.txt

# Copy project
COPY . /code

RUN mkdir media
