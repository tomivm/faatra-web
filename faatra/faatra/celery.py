import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'faatra.settings')

url = os.environ.get('REDIS_URL', 'localhost')
app = Celery('faatra', broker=f'redis://{url}:6379/0')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls every day
    # minute=0, hour=0
    sender.add_periodic_task(crontab(), close_informative_offer)

@app.task
def close_informative_offer():
    from incriptions.models import InformativeOffer
    from datetime import datetime

    now = datetime.now()
    InformativeOffer.objects.filter(due_date=now).update(is_cancelled=True)
    print("me ejecute")
