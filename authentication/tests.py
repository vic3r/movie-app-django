from django.test import TestCase
from datetime import date
from authentication.models import UserProfile

class UserProfileTestCase(TestCase):
    def setUp(self):
        UserProfile.objects.create_user(
            email='test@test.com',
            username='test',
            first_name='Adal',
            last_name='Ramones',
            password='pass',
        )
    
    def test_get_user(self):
        test = UserProfile.objects.get(username='test')
        self.assertEqual(test.first_name, 'Adal')
