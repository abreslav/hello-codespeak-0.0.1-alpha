import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
import json
import time


class HomeEndpointTestCase(TestCase):
    """Test cases for the home endpoint."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    @pytest.mark.timeout(30)
    def test_home_endpoint_get_success(self):
        """
        Test kind: endpoint_tests
        Original method: django_app.views.home

        Test that GET request to home endpoint returns successful response.
        """
        # Act
        response = self.client.get('/')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello from')
        self.assertContains(response, 'CodeSpeak!')
        self.assertContains(response, 'Django')
        self.assertContains(response, 'Tailwind CSS')

    @pytest.mark.timeout(30)
    def test_home_endpoint_uses_correct_template(self):
        """
        Test kind: endpoint_tests
        Original method: django_app.views.home

        Test that home endpoint uses the correct template.
        """
        # Act
        response = self.client.get('/')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'django_app/home.html')

    @pytest.mark.timeout(30)
    def test_home_endpoint_post_method(self):
        """
        Test kind: endpoint_tests
        Original method: django_app.views.home

        Test that POST request to home endpoint works (should be handled same as GET).
        """
        # Act
        response = self.client.post('/')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello from')
        self.assertContains(response, 'CodeSpeak!')

    @pytest.mark.timeout(30)
    def test_home_endpoint_response_headers(self):
        """
        Test kind: endpoint_tests
        Original method: django_app.views.home

        Test that home endpoint returns expected response headers.
        """
        # Act
        response = self.client.get('/')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')

    @pytest.mark.timeout(30)
    def test_home_endpoint_with_custom_headers(self):
        """
        Test kind: endpoint_tests
        Original method: django_app.views.home

        Test that home endpoint handles requests with custom headers.
        """
        # Act
        response = self.client.get('/', HTTP_USER_AGENT='TestAgent/1.0', HTTP_X_FORWARDED_FOR='127.0.0.1')

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello from')
        self.assertContains(response, 'CodeSpeak!')

    @pytest.mark.timeout(30)
    def test_home_endpoint_url_reverse(self):
        """
        Test kind: endpoint_tests
        Original method: django_app.views.home

        Test that home endpoint can be accessed via URL reverse lookup.
        """
        # Act
        url = reverse('home')
        response = self.client.get(url)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello from')
        self.assertContains(response, 'CodeSpeak!')
        self.assertEqual(url, '/')