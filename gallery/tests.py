from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.frank= Editor(first_name = 'frank', last_name ='gacheru', email ='francisgacheru2001@.com')
        
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.frank,Image))