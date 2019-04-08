FROM python:3

# Set environment variables
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /

# Install dependencies.
RUN pip install -r /requirements.txt

# Set work directory.
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# Copy project code.
COPY . /usr/src/app

EXPOSE 80
