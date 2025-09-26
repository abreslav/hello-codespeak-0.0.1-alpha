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


class SystemStatusEndpointTestCase(TestCase):
    """Test case for system_status view endpoint tests."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    @pytest.mark.timeout(30)
    def test_system_status_endpoint_get_request(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.system_status

        Test that GET request to system_status endpoint returns correct response.
        """
        url = reverse('system_status')
        response = self.client.get(url)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check response content type
        self.assertEqual(response['content-type'], 'text/html; charset=utf-8')

        # Check that response contains expected HTML content
        content = response.content.decode('utf-8')
        self.assertIn('System Status', content)
        self.assertIn('<title>System Status - CodeSpeak</title>', content)
        self.assertIn('Real-time system information', content)

        # Check for system information sections
        self.assertIn('Operating System', content)
        self.assertIn('Current Time', content)
        self.assertIn('CPU Usage', content)
        self.assertIn('Memory Usage', content)

        # Check for emoji icons
        self.assertIn('🖥️', content)
        self.assertIn('🕒', content)
        self.assertIn('⚡', content)
        self.assertIn('💾', content)

        # Check that system data is populated in the rendered template
        # The template variables should be replaced with actual values
        # Check for actual system information patterns
        import re

        # Check for OS information (should contain Linux, Windows, or Darwin)
        os_pattern = r'(Linux|Windows|Darwin|macOS)'
        self.assertRegex(content, os_pattern)

        # Check for CPU usage percentage (should be a number followed by %)
        cpu_pattern = r'\d+\.?\d*%'
        self.assertRegex(content, cpu_pattern)

        # Check for memory information (should contain GB)
        memory_pattern = r'\d+\.?\d* GB'
        self.assertRegex(content, memory_pattern)

        # Check for datetime format (YYYY-MM-DD HH:MM:SS)
        datetime_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
        self.assertRegex(content, datetime_pattern)

    @pytest.mark.timeout(30)
    def test_system_status_endpoint_post_request(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.system_status

        Test that POST request to system_status endpoint returns correct response.
        """
        url = reverse('system_status')
        response = self.client.post(url)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check response content type
        self.assertEqual(response['content-type'], 'text/html; charset=utf-8')

        # Check that response contains expected HTML content
        content = response.content.decode('utf-8')
        self.assertIn('System Status', content)

    @pytest.mark.timeout(30)
    def test_system_status_endpoint_with_custom_headers(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.system_status

        Test system_status endpoint with custom headers.
        """
        url = reverse('system_status')
        response = self.client.get(url, HTTP_X_CUSTOM_HEADER='test-value')

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check that response contains expected HTML content
        content = response.content.decode('utf-8')
        self.assertIn('System Status', content)

    @pytest.mark.timeout(30)
    def test_system_status_endpoint_response_structure(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.system_status

        Test that system_status endpoint returns properly structured HTML response.
        """
        url = reverse('system_status')
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

        # Check for main grid structure
        self.assertIn('grid-cols-1 md:grid-cols-2', content)

        # Check for navigation back to home
        self.assertIn('Back to Home', content)
        self.assertIn('href="/"', content)


class DbDemoEndpointTestCase(TestCase):
    """Test case for db_demo view endpoint tests."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    @pytest.mark.timeout(30)
    def test_db_demo_endpoint_get_request(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.db_demo

        Test that GET request to db_demo endpoint returns correct response.
        """
        url = reverse('db_demo')
        response = self.client.get(url)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check response content type
        self.assertEqual(response['content-type'], 'text/html; charset=utf-8')

        # Check that response contains expected HTML content
        content = response.content.decode('utf-8')
        self.assertIn('DB Demo', content)
        self.assertIn('<title>DB Demo - CodeSpeak</title>', content)
        self.assertIn('Interact with the database', content)

    @pytest.mark.timeout(30)
    def test_db_demo_endpoint_post_request_valid_data(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.db_demo

        Test that POST request to db_demo endpoint with valid data creates record and redirects.
        """
        from django_app.models import Demo

        # Count initial records
        initial_count = Demo.objects.count()

        url = reverse('db_demo')
        response = self.client.post(url, {
            'name': 'Test Demo',
            'description': 'Test description'
        })

        # Check redirect response
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('db_demo'))

        # Check that record was created
        self.assertEqual(Demo.objects.count(), initial_count + 1)

        # Check that the record has correct data
        demo = Demo.objects.filter(name='Test Demo').first()
        self.assertIsNotNone(demo)
        self.assertEqual(demo.name, 'Test Demo')
        self.assertEqual(demo.description, 'Test description')

    @pytest.mark.timeout(30)
    def test_db_demo_endpoint_post_request_invalid_data(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.db_demo

        Test that POST request to db_demo endpoint with invalid data shows error.
        """
        from django_app.models import Demo

        # Count initial records
        initial_count = Demo.objects.count()

        url = reverse('db_demo')

        # Test with missing name
        response = self.client.post(url, {
            'name': '',
            'description': 'Test description'
        })

        # Check response status code (no redirect, shows form again)
        self.assertEqual(response.status_code, 200)

        # Check that no record was created
        self.assertEqual(Demo.objects.count(), initial_count)

        # Check error message appears
        content = response.content.decode('utf-8')
        self.assertIn('Both name and description are required', content)

        # Test with missing description
        response = self.client.post(url, {
            'name': 'Test Demo',
            'description': ''
        })

        # Check response status code (no redirect, shows form again)
        self.assertEqual(response.status_code, 200)

        # Check that no record was created
        self.assertEqual(Demo.objects.count(), initial_count)

    @pytest.mark.timeout(30)
    def test_db_demo_endpoint_displays_existing_records(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.db_demo

        Test that db_demo endpoint displays existing Demo records.
        """
        from django_app.models import Demo

        # Create test records
        demo1 = Demo.objects.create(name='Demo 1', description='Description 1')
        demo2 = Demo.objects.create(name='Demo 2', description='Description 2')

        url = reverse('db_demo')
        response = self.client.get(url)

        # Check response status code
        self.assertEqual(response.status_code, 200)

        # Check that records appear in response
        content = response.content.decode('utf-8')
        self.assertIn('Demo 1', content)
        self.assertIn('Description 1', content)
        self.assertIn('Demo 2', content)
        self.assertIn('Description 2', content)

    @pytest.mark.timeout(30)
    def test_db_demo_endpoint_response_structure(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.db_demo

        Test that db_demo endpoint returns properly structured HTML response.
        """
        url = reverse('db_demo')
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

        # Check for form elements
        self.assertIn('<form', content)
        self.assertIn('method="post"', content)
        self.assertIn('name="name"', content)
        self.assertIn('name="description"', content)
        self.assertIn('type="submit"', content)

        # Check for navigation back to home
        self.assertIn('Back to Home', content)
        self.assertIn('href="/"', content)