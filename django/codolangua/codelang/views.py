from django.shortcuts import render
from django.http import HttpResponse

from codelang.models import Topic, Language


def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'codelang/index.html', context=data)


def show_python_page(request):
    language = Language.objects.get(title='Python')
    topics = Topic.objects.filter(programming_languages=language)
    data = {'title': f'Теория {language.title}',
            'topics': topics}
    return render(request, 'codelang/python-page.html', context=data)


def show_js_page(request):
    language = Language.objects.get(title='JavaScript')
    topics = Topic.objects.filter(programming_languages=language)
    data = {'title': f'Теория {language.title}',
            'topics': topics}
    return render(request, 'codelang/js-page.html', context=data)


def show_html_css_page(request):
    language = Language.objects.get(title='HTML/CSS')
    topics = Topic.objects.filter(programming_languages=language)
    data = {'title': f'Теория {language.title}',
            'topics': topics}
    return render(request, 'codelang/html-css-page.html', context=data)