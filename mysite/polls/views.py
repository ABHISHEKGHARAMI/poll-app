from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Questions
from django.template import loader
from django.shortcuts import get_object_or_404


def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
   
    
    context = {
        'latest_question_list' : latest_question_list
    }
    
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    questions = get_object_or_404(Questions,pk=question_id)
    return render(request,'polls/detail.html',{
        'questions' : questions
    })


def results(request,question_id):
    response = "You are looking at the result of the question %s"
    return HttpResponse(response % question_id)


def votes(request,question_id):
    return HttpResponse("you are voting for the question %s " %question_id)