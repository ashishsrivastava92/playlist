from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from greedy.models import Track, Genre
from django.db import models
from django.http import HttpResponse


# Create your views here.

# from django.http ifrom django.views.generic import ListView

class TracksList(ListView):
    model = Track
    paginate_by = 10
    template_name = 'track_list.html'

    # extra_context = None

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        genre = Genre.objects.all()
        context['gene'] = []
        for entry in genre:
            track_genre = entry.name
            context['gene'].append(track_genre)

        return context


class TracksDetail(DetailView):
    model = Track
    # template_name = 'greedy/track_detail.html'


class GenreList(ListView):
    model = Genre
    paginate_by = 10
    template_name = 'genre_list.html'


class GenreDetail(DetailView):
    model = Genre

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        genre_id = self.object.id
        genre = Genre.objects.get(id=genre_id)
        # genre = genre.name
        tracks = Track.objects.filter(genre=genre)
        context['tracks'] = tracks
        context['hello'] = genre_id
        # for entry in genre:
        #     track_genre = entry.name
        #     context['gene'].append(track_genre)

        return context


def index(request):
    return render(request, 'greedy/index.html')


def view_post(request, **kwargs):
    id = kwargs['id']
    if id:
        tracks = get_object_or_404(Track, id=id)
        return render(request, 'track_list.html', {'tracks': tracks})
    else:
        return render(request, 'track_list.html')
