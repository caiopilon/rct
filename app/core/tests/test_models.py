from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model


def sample_user(email="test@domain.com", password="testpass"):
    """"Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """"Test creating a new user with an email is successful"""
        email = "test@domain.com"
        password = "Testpass123"
        user = get_user_model().object.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
