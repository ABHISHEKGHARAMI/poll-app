from django.test import TestCase

# Create your tests here.

import datetime
from django.utils import timezone


from .models import Question

# class for the test
class QuestionModelTests(TestCase):
    def test_was_published_with_future_questions(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_questions = Question(pub_date=time)
        self.assertIs(future_questions.was_published_recently(),False)
