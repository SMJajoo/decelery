import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "decelery.settings") # celery to access settings in django project
app = Celery("decelery") # create a celery app
app.config_from_object("django.conf:settings", namespace="CELERY") # load celery settings from django settings
app.conf.task_routes = {'newapp.tasks.task1': {'queue':'queue1'}, 'newapp.tasks.task2': {'queue':'queue2'}}
app.autodiscover_tasks() # autodiscover tasks in the app
