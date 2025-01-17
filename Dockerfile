FROM python:3.13-slim

ARG DB_HOST
ARG DB_USER
ARG DB_PASS
ARG DB_NAME
ARG DB_PORT

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

ENV DB_HOST=${DB_HOST} \
    DB_USER=${DB_USER} \
    DB_PASS=${DB_PASS} \
    DB_PORT=${DB_PORT} \
    DB_NAME=${DB_NAME}

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "devtasktracker.wsgi:application", "--bind", "0.0.0.0:8000"]
