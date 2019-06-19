FROM python:3.6-alpine

LABEL maintainer="etienne.napoleone@gmail.com"

WORKDIR /thoughtful-investor

RUN apk add --no-cache gcc musl-dev openssl-dev libffi-dev

COPY ./thoughtful_investor ./thoughtful_investor
COPY ./assets ./assets
COPY pyproject.toml .
COPY poetry.lock .

RUN pip3 install poetry \
&&  poetry install

ENTRYPOINT ["poetry", "run", "thoughtful-investor"]
