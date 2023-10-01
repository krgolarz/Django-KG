from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies, name='all_movies'),
    path('<int:id>', views.movie_details, name='movie_details'),
    path('add',views.add_movie, name="add_movie"),
    path('collections', views.all_collections, name='all_collections'),
    path('collections/<int:id>,', views.collections_details, name='collections_details')
]
