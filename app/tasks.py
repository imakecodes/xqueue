import os

from celery import Celery

celery = Celery(__name__)
celery.conf.broker_url = os.getenv("CELERY_BROKER_URL", "amqp://localhost:5672")


@celery.task(name="publish")
def publish_message(*args, **kwargs):
    print(args, kwargs)
