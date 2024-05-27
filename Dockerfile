FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install --upgrade pip \
    &&pip install --no-cache-dir -r requirements.txt

COPY . /app/
## Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY ./entrypoint.sh .
RUN chmod 755 entrypoint.sh
ENTRYPOINT ["sh", "/app/entrypoint.sh"]