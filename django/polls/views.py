from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Question


def index(request):
    question_list = Question.objects.order_by('-create_date') #역순 정렬
    context = {'question_list': question_list}
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'polls/question_list.html', context)

def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/question_detail.html', context)