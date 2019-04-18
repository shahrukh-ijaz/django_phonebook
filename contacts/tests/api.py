from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class UserLoginAPIViewTestCase(APITestCase):

    def setUp(self):
        self.url = "http://127.0.0.1:8001/api/login"
        self.username = "shahrukh-ijaz31"
        self.password = "shahrukh31"
        self.email = "shahrukh@arbisoft.com"

    def test_authentication_without_password(self):
        User.objects.create_user(self.username, self.password)
        response = self.client.post(self.url, {"username": self.username}, format='multipart')
        self.assertEqual(400, response.status_code)

    def test_authentication_with_incorrect_password(self):
        User.objects.create_user(self.username, self.password)
        response = self.client.post(self.url, {"username": self.username, "password": "abc"}, format='json')
        self.assertEqual(400, response.status_code)

    def test_authentication_with_right_details(self):
        self.user = User.objects.create_user(username=self.username, password=self.password, email= self.email)
        response = self.client.post(self.url, {"username": self.username, "password": self.password}, format='multipart')
        self.assertEqual(200, response.status_code)


class ProfileAPIViewTestCase(APITestCase):

    def setUp(self):
        self.url = "http://127.0.0.1:8001/api/login"
        self.profile = "http://127.0.0.1:8001/api/profile"
        self.username = "shahrukh-ijaz31"
        self.password = "shahrukh31"
        self.email = "shahrukh@arbisoft.com"

    def test_get_profile_details(self):
        self.user = User.objects.create_user(username=self.username, password=self.password, email=self.email)
        response = self.client.post(self.url, {"username": self.username, "password": self.password},
                                    format='multipart')
        if response.status_code == 200:
            response = self.client.get(self.profile)
            self.assertEqual(200, response.status_code)
        else:
            self.assertFalse(200, response.status_code)

    def test_put_profile_details(self):
        self.user = User.objects.create_user(username=self.username, password=self.password, email=self.email)
        response = self.client.post(self.url, {"username": self.username, "password": self.password},
                                    format='multipart')
        if response.status_code == 200:
            response = self.client.get(self.profile, data={"id": 1, "first_name": "shahrukh ijaz", "last_name": "ijaz",
                                                           "username": self.username, "email": self.email},
                                       format='json')
            self.assertEqual(200, response.status_code)
        else:
            self.assertFalse(200, response.status_code)


class ContactsAPIViewTestCase(APITestCase):

    def setUp(self):
        self.url = "http://127.0.0.1:8001/api/login"
        self.contacts = "http://127.0.0.1:8001/api/contacts"
        self.username = "shahrukh-ijaz31"
        self.password = "shahrukh31"
        self.email = "shahrukh@arbisoft.com"

    def test_get_contacts(self):
        self.user = User.objects.create_user(username=self.username, password=self.password, email=self.email)
        response = self.client.post(self.url, {"username": self.username, "password": self.password},
                                    format='multipart')
        if response.status_code == 200:
            response = self.client.get(self.contacts)
            self.assertEqual(200, response.status_code)
        else:
            self.assertFalse(200, response.status_code)


