FROM python:3.8-alpine

COPY ./api /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN ls

ENTRYPOINT [ "flask", "run" ]
