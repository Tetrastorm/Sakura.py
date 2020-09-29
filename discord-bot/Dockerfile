FROM python:3

WORKDIR /var/www/app

COPY ./src/ .
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

CMD ["./run.py"]
