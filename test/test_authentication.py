from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Students-list')
        self.user = User.objects.create_user('user', password='123456')

    def test_check_user_authentication_with_correct_credentials(self):
        """Test that verifies user authentication with correct credentials"""
        user = authenticate(username='user', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_check_user_authentication_with_incorrect_username(self):
        """Test that verifies user authentication with incorrect username"""
        user = authenticate(username='user1', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_check_user_authentication_with_incorrect_password(self):
        """Test that verifies user authentication with incorrect password"""
        user = authenticate(username='user', password='123455')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_get_request_for_an_authorized_user(self):
        """Test that checks for an authorized GET request"""        
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_request_for_an_unauthorized_user(self):
        """Test that checks for an unauthorized GET request"""        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)