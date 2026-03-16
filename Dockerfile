FROM python:3.15-rc-alpine3.23

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest"]
