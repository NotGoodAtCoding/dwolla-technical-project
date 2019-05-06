FROM python:3.6.8-slim-stretch

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY server/ /server
WORKDIR server

EXPOSE 5000

ENV FLASK_APP=main.py
ENV FLASK_ENV=development

CMD ["flask", "run"]
