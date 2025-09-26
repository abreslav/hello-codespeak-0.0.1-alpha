import pytest
from django.test import TestCase
from django_app.models import Demo


class DemoModelTestCase(TestCase):
    """Test case for Demo model unit tests."""

    @pytest.mark.timeout(30)
    def test_demo_str_method(self):
        """
        Test kind: unit_tests
        Original method FQN: django_app.models.Demo.__str__

        Test that Demo.__str__ returns the name field value.
        """
        # Create a Demo instance with specific name
        demo = Demo(name="Test Demo", description="Test description")

        # Test that __str__ returns the name field
        self.assertEqual(str(demo), "Test Demo")

        # Test with different name
        demo2 = Demo(name="Another Demo", description="Another description")
        self.assertEqual(str(demo2), "Another Demo")

        # Test with empty name
        demo3 = Demo(name="", description="Some description")
        self.assertEqual(str(demo3), "")

        # Test with special characters in name
        demo4 = Demo(name="Demo with 🎉 emoji", description="Description")
        self.assertEqual(str(demo4), "Demo with 🎉 emoji")