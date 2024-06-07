from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import  F
from django.views import generic
from .models import Question, Choice
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from . import views


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
   
    
    context = {
        'latest_question_list' : latest_question_list
    }
    
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{
        'question' : question
    })


def results(request,question_id):
    questions  = get_object_or_404(Question,pk = question_id)
    return render(
        request,
        "polls/result.html",
        {
            'questions': questions
        }
    )


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = questions.choice_set.get(pk = request.POST['choice'])
        print(selected_choice)
    except (KeyError,Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                'question' : question,
                'error_message' : "you didn't select a choice" 
            }
        )
        
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))