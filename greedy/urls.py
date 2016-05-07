from django.conf.urls import url, include
from greedy import views
from tastypie.api import Api
from greedy.api import TrackResource, GenreResource, AjaxSearchResource

v1_api = Api(api_name='v1')
v1_api.register(TrackResource())
v1_api.register(GenreResource())
v1_api.register(AjaxSearchResource())

urlpatterns = [
                url(r'^api/', include(v1_api.urls)),
                url(r'^$', views.index,name='index'),
                url(r'^tracks/$', views.TracksList.as_view(), name = "track_list"),
                url(r'^track/(?P<pk>\d+)/$', views.TracksDetail.as_view(), name = 'track_details'),
                url(r'^genres/$', views.GenreList.as_view(), name = "genre_list"),
                url(r'^genre/(?P<pk>\d+)/$', views.GenreDetail.as_view(), name = 'genre_details'),

               ]