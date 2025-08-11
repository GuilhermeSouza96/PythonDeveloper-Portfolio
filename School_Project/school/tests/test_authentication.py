from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            password='admin'
        )
        self.url = reverse('Students-list')
    
    def test_authentication_of_correct_credentials(self):
        '''Test to verify authentication with correct credentials'''
        user = authenticate(username = 'admin', password = 'admin')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_authentication_of_incorrect_username(self):
        '''Test to verify authentication with incorrect username'''
        user = authenticate(username = 'admn', password = 'admin')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authentication_of_incorrect_password(self):
        '''Test to verify authentication with incorrect password'''
        user = authenticate(username = 'admin', password = 'admn')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authorized_get(self):
        '''Test to verify an authorized GET'''
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_get(self):
        '''Test to verify an unauthorized GET'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)