import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "decelery.settings") # celery to access settings in django project
app = Celery("decelery") # create a celery app
app.config_from_object("django.conf:settings", namespace="CELERY") # load celery settings from django settings

@app.task # decorator to make the function a celery task
def add_numbers():
    return

app.autodiscover_tasks() # autodiscover tasks in the app
