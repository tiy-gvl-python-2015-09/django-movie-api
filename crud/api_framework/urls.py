from django.conf.urls import include, url

from api_framework.views import MovieListView, MovieDetailView


urlpatterns = [
    url(r'^movie/$', MovieListView.as_view(), name="api_movie_list"),
    url(r'^movie/(?P<pk>\d+)/$', MovieDetailView.as_view(), name="api_movie_detail"),
]
