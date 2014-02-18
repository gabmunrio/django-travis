"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import os
from django.utils.unittest import skipIf

from django.test import TestCase
from polls.models import Choice, Poll
import datetime
from django.utils import timezone


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class PollsMethodTest(TestCase):
    def test_poll_was_published_recently(self):
        poll = Poll(pub_date=(timezone.now() - datetime.timedelta(days=1)))
        self.assertEqual(poll.was_published_recently(), False)


@skipIf(os.environ['INTERFACE'] == "1", 'We need to check the phantomjs execution')
class ChoiceMethodTest(TestCase):
    def test_choice_positive(self):
        choice = Choice(votes=1)
        self.assertEqual(choice.votes > 0, True)

    def test_choice_negative(self):
        choice = Choice(votes=-1)
        self.assertEqual(choice.votes < 0, True)

    def test_choice_positive_and_return_false(self):
        choice = Choice(votes=1)
        self.assertEqual(choice.votes < 0, False)
