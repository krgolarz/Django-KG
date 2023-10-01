from django.shortcuts import render, reverse, get_object_or_404, redirect
from . import models
# Create your views here.
from django.http import HttpResponseRedirect
from django.db.models import Count
from . import models
from .forms import MovieForm


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
        print(request.POST.get('title'))
        print(request.POST.get('cast'))
        print(request.POST.get('release_date'))
        print(request.body)

        '''return HttpResponseRedirect(reversed('all_movies'))'''
        return redirect('all_movies')
    movie_form = MovieForm()
    return render(request, 'movie/add_movie.html', {'movie_form': movie_form})


def all_collections(request):
    found_collections = models.MovieCollection.objects.all().annotate(movies_count=Count('movies'))
    return render(request, 'movie/all_collections.html', {'collections': found_collections})


def collections_details(request, id):
    found_collection = get_object_or_404(models.MovieCollection, id=id)
    return render(request, 'movie/collecion_detalis.html', {'collection': found_collection})
