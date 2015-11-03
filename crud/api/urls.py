from django.conf.urls import include, url

from api.views import hello, api_movie_list_create_view, api_detail_view

urlpatterns = [
    url(r'hello/', hello),
    url(r'movie/$', api_movie_list_create_view, name="api_movie_list_create_view"),
    url(r'movie/(?P<model_pk>\d+)/', api_detail_view, name="api_detail_view"),

]
