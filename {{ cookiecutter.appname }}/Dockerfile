FROM python:3.10.8-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN python -m pip install -r requirements.txt

COPY ./src /app

WORKDIR /app

COPY ./entrypoint.sh /
COPY ./test_alive.py /

ENTRYPOINT ["sh", "/entrypoint.sh"]