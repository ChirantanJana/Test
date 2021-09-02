from django.conf.urls import url
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from travel.views import destinations, index

class TestUrls(SimpleTestCase):

    def test_index_url_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)
    
    def test_index_url_resolved(self):
        url = reverse('destinations')
        self.assertEqual(resolve(url).func, destinations)
    


    
