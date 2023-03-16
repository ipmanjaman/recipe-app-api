"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    """Test the calc module."""
    def test_add_numbers(self):
        """Test adding number together."""
        res = calc.add(5,6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """ Test subtracting number together. """
        res = calc.sub(3,4)
        self.assertEqual(res, -1)
