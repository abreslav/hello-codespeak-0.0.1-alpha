import pytest
from django.test import TestCase, Client
from django.urls import reverse
import json
import time


class HelloEndpointTestCase(TestCase):
    """Test case for hello view endpoint tests."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    @pytest.mark.timeout(30)
    def test_hello_endpoint_get_request(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.hello

        Test that GET request to hello endpoint returns correct response.
        """
        url = reverse('hello')
        response = self.client.get(url)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check response content type
        self.assertEqual(response['content-type'], 'text/html; charset=utf-8')

        # Check that response contains expected HTML content
        content = response.content.decode('utf-8')
        self.assertIn('CodeSpeak!', content)
        self.assertIn('<title>Hello from CodeSpeak</title>', content)
        self.assertIn('Welcome to your simple Django web application', content)
        self.assertIn('👋', content)

    @pytest.mark.timeout(30)
    def test_hello_endpoint_post_request(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.hello

        Test that POST request to hello endpoint returns correct response.
        """
        url = reverse('hello')
        response = self.client.post(url)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check response content type
        self.assertEqual(response['content-type'], 'text/html; charset=utf-8')

        # Check that response contains expected HTML content
        content = response.content.decode('utf-8')
        self.assertIn('CodeSpeak!', content)

    @pytest.mark.timeout(30)
    def test_hello_endpoint_with_custom_headers(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.hello

        Test hello endpoint with custom headers.
        """
        url = reverse('hello')
        response = self.client.get(url, HTTP_X_CUSTOM_HEADER='test-value')

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check that response contains expected HTML content
        content = response.content.decode('utf-8')
        self.assertIn('CodeSpeak!', content)

    @pytest.mark.timeout(30)
    def test_hello_endpoint_with_query_parameters(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.hello

        Test hello endpoint with query parameters.
        """
        url = reverse('hello')
        response = self.client.get(url + '?param=value')

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check that response contains expected HTML content
        content = response.content.decode('utf-8')
        self.assertIn('CodeSpeak!', content)

    @pytest.mark.timeout(30)
    def test_hello_endpoint_response_structure(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.hello

        Test that hello endpoint returns properly structured HTML response.
        """
        url = reverse('hello')
        response = self.client.get(url)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check HTML structure
        content = response.content.decode('utf-8')
        self.assertIn('<!DOCTYPE html>', content)
        self.assertIn('<html lang="en">', content)
        self.assertIn('<head>', content)
        self.assertIn('<body', content)
        self.assertIn('</body>', content)
        self.assertIn('</html>', content)

        # Check for Tailwind CSS
        self.assertIn('cdn.tailwindcss.com', content)

        # Check for main elements
        self.assertIn('<h1', content)
        self.assertIn('CodeSpeak', content)