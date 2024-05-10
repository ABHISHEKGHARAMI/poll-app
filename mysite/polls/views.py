from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world,you are in polls index")


def detail(request,question_id):
    response = "you are looking at the result of the question %s."
    return HttpResponse(response % question_id)
