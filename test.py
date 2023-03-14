import unittest

from src import find_components, read


class TestAlg(unittest.TestCase):
    def test_works_with_1_component(self):
        self.assertEqual(find_components(read("resources/in.txt")), [[1, 2, 3, 4]])

    def test_works_with_2_components(self):
        self.assertEqual(find_components(read("resources/in2.txt")), [[1, 2], [3]])

    def test_works_with_3_components(self):
        self.assertEqual(find_components(read("resources/in3.txt")), [[1, 3, 4, 5], [2, 7], [6]])

    def test_works_with_empty_file(self):
        self.assertEqual(find_components(read("resources/in4.txt")), [])

    def test_works_with_no_components(self):
        self.assertEqual(find_components(read("resources/in5.txt")), [])

    def test_works_with_no_edges(self):
        self.assertEqual(find_components(read("resources/in6.txt")), [[1], [2], [3]])
