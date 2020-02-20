import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'podcast.settings')

# For opportunity to use in on Windows.
# celery -A podcast worker -l info
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('podcast')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Monitoring via Flower on the address http://localhost:5555/dashboard
# celery -A podcast flower