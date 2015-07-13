"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from movie.views import MovieListView, MovieCreateView, MovieDeleteView, MovieDetailView

urlpatterns = [
    url(r'^movie_list/', MovieListView.as_view(), name="movie_list"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create_movie/', MovieCreateView.as_view(), name="create_movie"),
    url(r'^delete_movie/(?P<pk>\d+)/',MovieDeleteView.as_view(), name="delete_movie"),
    url(r'^movie_detail/(?P<pk>\d+)/',MovieDetailView.as_view(), name="movie_detail")

]
