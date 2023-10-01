from django.shortcuts import render, reverse
from . import models
# Create your views here.
from django.http import HttpResponseRedirect

from . import models



def all_movies(request):
    title = request.GET.get('title')
    if title:
        movies = models.Movie.objects.filter(title__contains=title)[:20]
    else:
        movies = models.Movie.objects.all()[:20]
    return render(request, 'movie/all_movies.html', {'movies': movies, 'title_filter' : title})


def movie_details(request, id):
    found_movie = models.Movie.objects.get(pk=id)
    return render(request, 'movie/movie_details.html', {'movie': found_movie})
