from django.utils import timezone
from celery import shared_task

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .models import Scrape


def do_scrape(url):
    options = webdriver.ChromeOptions()
    options.add_argument(" - incognito")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    browser = webdriver.Chrome(
        executable_path="/usr/local/bin/chromedriver", chrome_options=options
    )

    browser.get(url)
    timeout = 10

    try:
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(
                (
                    By.TAG_NAME,
                    "body",
                )
            )
        )
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()
        return

    el = browser.find_element_by_tag_name("body")
    words = el.text.split()
    browser.close()

    return words


@shared_task
def scrape(scrape_id: int):
    try:
        obj = Scrape.objects.get(id=scrape_id)
    except Scrape.DoesNotExist:
        return

    words = do_scrape(obj.url)
    print(f'Found {len(words)} words in {obj.url}')
    obj.completed_at = timezone.now()
    obj.save()
