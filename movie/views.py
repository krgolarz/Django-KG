from django.shortcuts import render, reverse, get_object_or_404, redirect
from . import models
# Create your views here.
from django.http import HttpResponseRedirect
from django.db.models import Count
from . import models
from .forms import MovieForm, MovieFormTwo


def all_movies(request):
    title = request.GET.get('title')
    if title:
        movies = models.Movie.objects.filter(title__contains=title)[:20]
    else:
        movies = models.Movie.objects.all()[:20]
    return render(request, 'movie/all_movies.html', {'movies': movies, 'title_filter': title})


def movie_details(request, id):
    found_movie = models.Movie.objects.get(pk=id)
    return render(request, 'movie/movie_details.html', {'movie': found_movie})


def add_movie(request):
    if request.method == 'POST':
        new_movie_data = MovieFormTwo(request.POST)

        if new_movie_data.is_valid():
            '''#jezeli poprawny'''
            movie_data = new_movie_data.cleaned_data
            models.Movie.create_from_form(movie_data)

        '''return HttpResponseRedirect(reversed('all_movies'))'''
        return redirect('all_movies')

    else:
        new_movie_data = MovieFormTwo()

    return render(request, 'movie/add_movie.html', {'movie_form': new_movie_data})


def all_collections(request):
    found_collections = models.MovieCollection.objects.all().annotate(movies_count=Count('movies'))
    return render(request, 'movie/all_collections.html', {'collections': found_collections})


def collections_details(request, id):
    found_collection = get_object_or_404(models.MovieCollection, id=id)
    return render(request, 'movie/collecion_detalis.html', {'collection': found_collection})
