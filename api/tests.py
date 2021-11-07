from django.test import TestCase, RequestFactory
from .views import BookAPIView

class GetBookTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_details(self):
        request = self.factory.get('/api/')
        response = BookAPIView.as_view()(request)
        self.assertEqual(response.status_code,200)