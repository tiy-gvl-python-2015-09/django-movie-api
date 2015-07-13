from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
from movie.models import Movie


class ListViewTests(TestCase):

    def setUp(self):
        self.top_gun = Movie.objects.create(title="Top gun")
        self.fast_times = Movie.objects.create(title="fast times")
        self.stripes = Movie.objects.create(title="stripes")

    def test_movie_list_view_includes_all_movies_in_database(self):
        response = self.client.get("/movie_list/")
        self.assertTrue("Top gun" in str(response.content))
        movie_list = list(response.context)[0]['object_list']
        self.assertTrue(self.top_gun in movie_list)
        self.assertCountEqual(movie_list, Movie.objects.all())


class DeleteViewTests(TestCase):

    def setUp(self):
        self.top_gun = Movie.objects.create(title="Top gun")
        self.fast_times = Movie.objects.create(title="fast times")
        self.stripes = Movie.objects.create(title="stripes")

    def test_delete_view_will_delete_individual_movie(self):
        response = self.client.get("/movie_list/")
        self.assertTrue("Top gun" in str(response.content))

        delete_response = self.client.post(reverse("delete_movie", kwargs={"pk": self.top_gun.pk}))

        response = self.client.get("/movie_list/")
        self.assertFalse("Top gun" in str(response.content))
