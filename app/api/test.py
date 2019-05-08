from django.test import TestCase
from api.calc import add, substract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """ test 2 numbers sum"""
        self.assertEqual(add(3, 8), 11)

    def test_substraction_numbers(self):
        """ test substraction 2 numbers """
        self.assertEqual(substract(11, 6), 5)
