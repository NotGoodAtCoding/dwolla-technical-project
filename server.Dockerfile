FROM python:3.6.8-slim-stretch

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY server/ /server
WORKDIR server
ENV PATH=$PATH:/server

EXPOSE 5000

CMD ["python", "-m", "main"]
