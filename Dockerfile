FROM python:3.7-slim-stretch
ENV PYTHONUNBUFFERED 1

WORKDIR app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

EXPOSE 5432
COPY . .
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]