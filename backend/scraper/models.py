from django.db import models


class Scrape(models.Model):
    url = models.URLField(null=False, blank=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    completed_at = models.DateTimeField(null=True, blank=False)
    error = models.BooleanField(default=False, null=False)


class WordCount(models.Model):
    scrape = models.ForeignKey(
        Scrape, on_delete=models.CASCADE, related_name="words"
    )
    word = models.CharField(max_length=50)
    count = models.BigIntegerField()
