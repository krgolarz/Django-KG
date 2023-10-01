import csv

from django.db import models


class PublishPlace(models.Model):
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)


class Book(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
    vote_count = models.IntegerField()
    vote_average = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.CharField(max_length=255, null=True)
    publish_place = models.OneToOneField(PublishPlace, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"
