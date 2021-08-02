from django.utils import timezone
from celery import shared_task

from .models import Scrape
from .scraper import scrape_page


@shared_task
def scrape(scrape_id: int):
    try:
        obj = Scrape.objects.get(id=scrape_id)
    except Scrape.DoesNotExist:
        return

    try:
        text = scrape_page(obj.url)
        obj.completed_at = timezone.now()
    except Exception as e:
        obj.error = True
    finally:
        obj.save()
