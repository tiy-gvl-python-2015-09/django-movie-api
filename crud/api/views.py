from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from movie.models import Movie


def hello(request):
    all_movies = Movie.objects.all()
    serialized_data = serializers.serialize("json", all_movies)
    return HttpResponse(serialized_data, content_type="application/json")


@csrf_exempt
def api_movie_list_create_view(request):
    if request.method == "GET":
        qs = Movie.objects.all()
        return HttpResponse(serializers.serialize("json", qs), content_type="application/json")
    elif request.method == "POST":
        data = request.POST
        movie = Movie.objects.create(title=data['title'])
        return HttpResponse(serializers.serialize("json", [movie]), status=201, content_type="application/json")


@csrf_exempt
def api_detail_view(request, model_pk):
    if request.method == "POST":
        return HttpResponse("[]", status=409, content_type="application/json")
    if request.method == "PUT":
        model_detail_object = Movie.objects.get(id=model_pk)
        data = QueryDict(request.body)
        print(data,"IN PUT")

    model_detail_object = Movie.objects.filter(id=model_pk)
    if model_detail_object:
        return HttpResponse(serializers.serialize("json", model_detail_object), content_type="application/json")
    return HttpResponse("[]", content_type="application/json", status=404)
