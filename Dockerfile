FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requeriments.txt
RUN pip install --updrage accelerate
RUN pip install -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]