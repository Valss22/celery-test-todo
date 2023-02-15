FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1 \
    REDIS_URL=redis://redis:6379/0 \
    CELERY_BROKER_URL=redis://redis:6379/0 \
    CELERY_RESULT_BACKEND=redis://redis:6379/0 \
    DJANGO_SETTINGS_MODULE=config.settings

EXPOSE 8000

CMD ["bash", "run.sh"]
