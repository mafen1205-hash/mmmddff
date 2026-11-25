import unittest
from discount import calculate_discount

class TestDiscount(unittest.TestCase):
    def test_main_case(self):
        self.assertEqual(calculate_discount(1000, 20), 800.0)

    def test_boundary_zero(self):
        self.assertEqual(calculate_discount(500, 0), 500.0)

    def test_error_invalid(self):
        with self.assertRaises(ValueError):
            calculate_discount(1000, -5)

if __name__ == "__main__":
    unittest.main()
