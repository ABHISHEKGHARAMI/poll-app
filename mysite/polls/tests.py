from django.test import TestCase

# Create your tests here.

import datetime
from django.utils import timezone
from django.urls import reverse


from .models import Question

# class for the test
class QuestionModelTests(TestCase):
    def test_was_published_with_future_questions(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_questions = Question(pub_date=time)
        self.assertIs(future_questions.was_published_recently(),False)
        
    def test_was_published_with_old_questions(self):
        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(),True)
        
    def test_was_published_with_recent_questions(self):
        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(),True)
        
def create_Question(question_text,days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=days)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No polls available")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])
        
