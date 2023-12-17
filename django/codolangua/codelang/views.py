from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from codelang.models import Topic, Language


def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'codelang/index.html', context=data)


@login_required
def show_python_page(request):
    language = Language.objects.get(title='Python')
    topics = Topic.objects.filter(programming_languages=language)
    # for i in Topic.objects.filter(pk__gt=35):
    #     language.topic.add(i)
    i = 1
    for slug in slugs.splitlines():

        Topic.objects.filter(pk=i).update(topic_slug=slug)

        i += 1
    data = {'title': f'Теория {language.title}',
            'topics': topics}
    return render(request, 'codelang/python-page.html', context=data)


@login_required
def show_js_page(request):
    language = Language.objects.get(title='JavaScript')
    topics = Topic.objects.filter(programming_languages=language)
    data = {'title': f'Теория {language.title}',
            'topics': topics}
    return render(request, 'codelang/js-page.html', context=data)


@login_required
def show_html_css_page(request):
    language = Language.objects.get(title='HTML/CSS')
    topics = Topic.objects.filter(programming_languages=language)
    data = {'title': f'Теория {language.title}',
            'topics': topics}
    return render(request, 'codelang/html-css-page.html', context=data)


def show_topic_page(request, python_slug):
    topic = get_object_or_404(Topic, topic_slug=python_slug)
    t = {}
    i = 1
    for paragraphs in topic.topic_text.splitlines():
        t[f'paragraph{i}'] = paragraphs
        i += 1
    print(t)

    if python_slug == 'introduction-to-python':
        data = {'title': topic.topic_title,
                'topics': topic,
                'text': t,
                }
    else:
        data = {'title': topic.topic_title,
                'topics': topic,
                'text': t,
                }

    return render(request, 'codelang/topic-page.html', context=data)


def show_registration_page(request):
    data = {'title': 'Регистрация'}
    return render(request, 'codelang/reg_form.html', context=data)


def authorization(request):
    data = {'title': 'Главная страница'}
    return render(request, 'codelang/index.html', context=data)

