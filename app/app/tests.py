"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module."""
    # Arrange
    # variables (preparing..)

    # Act
    def test_add_numbers(self):
        """Test adding numbers together."""
        """Test First Development. TDD(Test Driven Development)"""
        # Act
        res = calc.add(5, 6)

        # Assert
        self.assertEqual(res, 11)