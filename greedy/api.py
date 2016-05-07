from tastypie.resources import ModelResource, Resource
from tastypie import fields
from django.conf.urls import url
from greedy.models import Track, Genre
from django.http.response import HttpResponse
from django.db import models
import json
from tastypie.utils import trailing_slash
import urlparse


class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'Genres'

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/add%s" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('add_genre'), name="add_genre"),
            url(r"^(?P<resource_name>%s)/edit/(?P<genre_id>\d+)%s" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('edit_genre'), name="edit_genre"),
        ]

    def add_genre(self, request, **kwargs):
        try:
            load = (urlparse.parse_qs(request.body))
            genre_name = load.get('Genre')[0]
            genre_context = load.get('Context')[0]
            genre = Genre.objects.create(name=genre_name, context=genre_context)
            genre.save()
            data = {'status': 200, 'message': 'Genre added successfully'}
        except:
            data = {'status': 500, 'message': 'Genre Already exists'}
        return HttpResponse(json.dumps(data), content_type="application/json")

    def edit_genre(self, request, **kwargs):
        try:
            genre_id = kwargs['genre_id']
            load = (urlparse.parse_qs(request.body))
            genre_name = load.get('Genre')[0]
            genre_context = load.get('Context')[0]
            genre = Genre.objects.get(id=genre_id)
            genre.name = genre_name
            genre.context = genre_context
            genre.save()
            data = {'status': 200, 'message': 'Genre updated successfully'}
        except:
            data = {'status': 500, 'message': 'Error In Data'}
        return HttpResponse(json.dumps(data), content_type="application/json")


class TrackResource(ModelResource):
    genre = fields.ForeignKey(GenreResource, 'genre')

    class Meta:
        queryset = Track.objects.all()
        resource_name = 'Tracks'
        always_return_data = True

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/adds%s" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('add_t'), name="add_t"),
            url(r"^(?P<resource_name>%s)/edit/(?P<track_id>\d+)%s" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('edit_track'), name="edit_track"),
        ]

    def add_t(self, request, **kwargs):
        try:
            load = (urlparse.parse_qs(request.body))
            song_name = load.get('Song')[0]
            genre_name = load.get('Genre')[0]
            genre = Genre.objects.get(name=genre_name)
            track = Track.objects.create(name=song_name, genre=genre)
            track.save()
            data = {'status': 200, 'message': 'Song updated successfully'}
        except:
            data = {'status': 500, 'message': 'Error In Data'}
        return HttpResponse(json.dumps(data), content_type="application/json")

    def edit_track(self, request, **kwargs):
        try:
            track_id = kwargs['track_id']
            load = (urlparse.parse_qs(request.body))
            song_name = load.get('Song')[0]
            genre_name = load.get('Genre')[0]
            genre = Genre.objects.get(name=genre_name)
            track = Track.objects.get(id=track_id)
            track.name = song_name
            track.genre = genre
            track.save()
            data = {'status': 200, 'message': 'Song updated successfully'}
        except:
            data = {'status': 500, 'message': 'Error In Data'}
        return HttpResponse(json.dumps(data), content_type="application/json")


class AjaxSearchResource(Resource):
    class Meta:
        resource_name = 'ajaxsearch'
        allowed_methods = ['post']
        always_return_data = True

    def post_list(self, request, **kwargs):
        phrase = request.POST.get('q')
        if phrase:
            tracks = list(Track.objects.filter(name__icontains=phrase).values('id', 'name'))
        return self.create_response(request, {'tracks': tracks})