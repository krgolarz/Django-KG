import csv

from django.db import models

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
    vote_count = models.IntegerField()
    vote_average = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.title},{self.release_date}'

    '''makemigrations'''
    @staticmethod
    def get_all():
        movies_arr = []

        with open('movie/movies_small.csv', 'r', encoding='utf-8') as input_file:
            input_file.readline()
            reader = csv.reader(input_file, delimiter=',')

            for row in reader:
                movies_arr.append(Movie(row[1], row[5], row[6], row[7], row[8], row[10],row[11], row[12], row[13], row[14], row[15], row[16], row[17] ))

        return movies_arr

    @staticmethod
    def get_movie_by_tbdb_id(tmdb_id):
        all_movies = Movie.get_all()
        for movie in all_movies:
            if movie.tmdb_id == tmdb_id:
                return movie
        return None


class Book(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
    vote_count = models.IntegerField()
    vote_average = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f"{self.title}"

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