FROM python:3.6.8-slim-stretch

ARG HOSTNAME=localhost
ENV HOSTNAME=$HOSTNAME

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY client/ /client
WORKDIR client

CMD ["python", "main.py"]
