from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Questions, Choice
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse


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
    questions  = get_object_or_404(Questions,pk = question_id)
    return render(
        request,
        'polls/result.html',
        {
            'questions': questions
        }
    )


def votes(request,question_id):
    questions = get_object_or_404(Questions,pk=question_id)
    try:
        selected_choice = questions.choice_set.get(pk = request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(
            request,
            'polls:detail.html',
            {
                'questions' : questions,
                'error_message' : "you didn't select a choice" 
            }
        )
        
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        
        return HttpResponse(
            reverse('polls:result',args=(questions.id))
        )