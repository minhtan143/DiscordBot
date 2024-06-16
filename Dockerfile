FROM python:3.12.4-alpine3.20

WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY /src .
CMD [ "python", "main.py" ]
