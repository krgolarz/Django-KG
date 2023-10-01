import csv

from django.db import models
from django.core.validators import MinLengthValidator


class MovieStatistics(models.Model):
    vote_count = models.IntegerField()
    vote_average = models.DecimalField(max_digits=5, decimal_places=2)


# Create your models here.
class Movie(models.Model):
    tmdb_id = models.CharField(max_length=15)
    title = models.CharField(max_length=1000)
    cast = models.CharField(max_length=1000)
    homepage = models.URLField()
    director = models.CharField(max_length=1000)
    keywords = models.CharField(max_length=1000)
    overview = models.TextField()
    runtime_minutes = models.IntegerField()
    genres = models.CharField(max_length=1000)
    production_companies = models.CharField(max_length=1000)
    release_date = models.DateField()
    statistics = models.OneToOneField(MovieStatistics, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title},{self.release_date}'


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class MovieCollection(models.Model):
    name = models.CharField(max_length=255, validators=[
        MinLengthValidator(4)
    ])
    creation_date = models.DateField()
    update_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name()

'''makemigrations'''

'''
Movie.objects.filter(title__startswith='Jurassic')
Movie.objects.filter(title__contains='Jurassic', vote_average__gt = 7)
from django.db.models import Q
Book.objects.filter(Q(title__startswith='lotr')|Q(title__startswith='alice'))
Book.objects.filter(Q(title__startswith='lotr')|Q(title__startswith='alice'),Q(vote_count__gte=1000))
Book.objects.filter(Q(title__startswith='lotr')|Q(title__startswith='alice'),Q(vote_count__gte=1000))
from django.db.models import Avg
books_aggregate_info = all_books.aggregate(Avg("vote_count"),Avg("vote_average"))
from django.db.models import Min, Max
books_aggregate_info = all_books.aggregate(Avg("vote_count"),Avg("vote_average"), Max("vote_count"), Min("vote_count"))

'''
