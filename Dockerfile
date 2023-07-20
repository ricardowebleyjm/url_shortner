# pull official base image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update  \
    && apt-get -y install gcc libssl-dev default-libmysqlclient-dev libmagic1 \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt 

WORKDIR /code
COPY entrypoint.sh /src/
COPY . /code

EXPOSE 8000
ENTRYPOINT ["sh", "entrypoint.sh"]