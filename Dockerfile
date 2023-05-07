FROM python:3.8-alpine3.17
RUN apk update; apk add mariadb-dev gcc musl-dev
RUN pip install mariadb