from django.shortcuts import render
from django.http import HttpResponse

from codelang.models import Topics


def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'codelang/index.html', context=data)


def python(request):
    topics = Topics.objects.all()
    data = {'title': 'Теория Python',
            'topics': topics}
    return render(request, 'codelang/python-page.html', context=data)
