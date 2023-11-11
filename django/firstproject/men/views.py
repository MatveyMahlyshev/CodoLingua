import django.http
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, QueryDict, HttpResponseRedirect
from datetime import datetime
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''(англ. Angelina Jolie[7], при рождении 
    Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — 
    американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй 
    воли ООН. Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд 
    выигравшая премию) и двух «Премий Гильдии киноактёров США».''', 'is_published': True},
    {'id': 2, 'title': 'Джонни Депп', 'content': 'Биография Джонни Деппа', 'is_published': True},
    {'id': 3, 'title': 'Леонардо Ди Каприо', 'content': 'Биография Леонардо Ди Каприо', 'is_published': False},
]

cats_db = [
    {'id': 1, 'name': 'Кино'},
    {'id': 2, 'name': 'Музыка'},
    {'id': 3, 'name': 'Спорт'},
]


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db,
            'cat_selected': 0,
            }
    return render(request, 'men/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def about(request):
    return render(request, 'men/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def add_page(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_category(request, cat_id):
    data = {'title': 'Отображение по рубрикам',
            'menu': menu,
            'posts': data_db,
            'cat_selected': cat_id,
            }
    return render(request, 'men/index.html', context=data)