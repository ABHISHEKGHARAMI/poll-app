from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world,you are in polls index")


def detail(request,question_id):
    return HttpResponse("You're looking at the question %s" %question_id)


def results(request,question_id):
    response = "You are looking at the result of the question %s"
    return HttpResponse(response % question_id)


def votes(request,question_id):
    return HttpResponse("you are voting for the question %s " %question_id)