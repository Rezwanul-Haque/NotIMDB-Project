from django.test import TestCase
from django.test.client import RequestFactory
from django.urls.base import reverse

from movies.models import Movie
from movies.views import MovieListView

# Create your tests here.
class MovieListPaginationTestCase(TestCase):
    ACTIVE_PAGINATION_HTML = """
        <li class="page-item active">
            <a href="{}?page={}" class="page-link">{}</a>
        </li>
        """
    
    def setUp(self):
        for i in range(15):
            Movie.objects.create(title='Title {}'.format(i), year=1990 + i, runtime=100)
        
    def testFirstPage(self):
        movie_list_path = reverse('movies:movie_list')
        request = RequestFactory().get(path=movie_list_path)
        response = MovieListView.as_view()(request)

        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context_data['is_paginated'])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(
                movie_list_path, 1, 1
            ),
            response.rendered_content
        )