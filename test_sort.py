import unittest
from sort import sort

class TestSort(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")

    def test_bulky(self):
        self.assertEqual(sort(200, 50, 50, 10), "SPECIAL")

    def test_heavy(self):
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")

    def test_rejected(self):
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")

    def test_edge_bulky_volume(self):
        self.assertEqual(sort(100, 100, 100, 19), "SPECIAL")  # volume = 1,000,000

    def test_edge_bulky_dimension(self):
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")  # dimension = 150

    def test_edge_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")  # mass = 20

if __name__ == "__main__":
    unittest.main()
