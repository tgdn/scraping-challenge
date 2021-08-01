from rest_framework import serializers

from .models import Scrape, WordCount


class ScrapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrape
        fields = [
            "id",
            "url",
            "words",
            "created_at",
            "completed_at",
        ]

        read_only_fields = [
            "id",
            "words",
            "created_at",
            "completed_at",
        ]


class WordCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordCount
        fields = [
            "id",
            "scrape",
            "word",
            "count",
        ]

        read_only_fields = [
            "id",
            "scrape",
            "word",
            "count",
        ]
