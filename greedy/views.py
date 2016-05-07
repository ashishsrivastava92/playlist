from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from greedy.models import Track, Genre

class TracksList(ListView):
    model = Track
    paginate_by = 10
    template_name = 'track_list.html'

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
        tracks = Track.objects.filter(genre=genre)
        context['tracks'] = tracks
        return context


def index(request):
    return render(request, 'greedy/index.html')
