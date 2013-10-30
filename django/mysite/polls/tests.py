"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from polls.models import Choice

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ChoiceMethodTest(TestCase):
	def test_choice_negative(self):
		choice = Choice(votes=1)
		self.assertEqual(choice.votes > 0, True)
