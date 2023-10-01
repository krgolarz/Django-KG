import csv

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
    vote_count = models.IntegerField()
    vote_average = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.title}"



