from django.urls import path
from movie_app.views import *

urlpatterns = [
    path('category/', CategoryView.as_view(), name="category"),
    path('category/<str:name>/movies/', MovieListView.as_view(), name="movie_list"),
    path('category/<str:name>/movies/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('watch/movie/<int:id>/', MovieView.as_view(), name="watch_movie"),
    path('category/<str:name>/series/', SeriesListView.as_view(), name="series_list"),
    path('category/<str:name>/series/<int:pk>/', SeasonListView.as_view(), name="season_list"),
    path('season/<int:id>/', SeasonDetailView.as_view(), name="season_detail"),
]