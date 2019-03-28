from django.shortcuts import render
from django.views.generic import ListView, DetailView

from movies.models import Movie

# Create your views here.
class MovieListView(ListView):
    model = Movie
    paginate_by = 4


class MovieDetailView(DetailView):
    model = Movie
