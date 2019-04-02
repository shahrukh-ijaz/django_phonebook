from celery import Celery
import os
from phone_book import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phone_book.settings')
app = Celery('phone_book')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
