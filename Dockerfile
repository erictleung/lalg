FROM python:3

RUN mkdir -p /var/app
WORKDIR /var/app
COPY . /var/app

# install numpy and required packages
RUN pip install numpy && \
    pip install .

