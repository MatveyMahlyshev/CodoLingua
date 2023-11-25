from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'codelang/index.html', context=data)


def python(request):
    data = {'title': 'Теория Python'}
    return render(request, 'codelang/python-page.html', context=data)
