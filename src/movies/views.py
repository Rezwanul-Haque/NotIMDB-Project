from django.shortcuts import render
from django.views.generic import ListView, DetailView

from movies.models import Movie

# Create your views here.
class MovieListView(ListView):
    model = Movie


class MovieDetailView(DetailView):
    model = Movie
