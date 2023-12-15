from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from codelang.models import Topic, Language


def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'codelang/index.html', context=data)


lines ='''Введение в Python:Установка, первые шаги, синтаксис, типы данных, переменные, операторы 
Управляющие конструкции:if, else, elif, циклы for, while 
Функции:Объявление, вызов, аргументы, возвращаемое значение 
Операторы:Арифметические, сравнения, логические, присваивания 
Строки:Объявление, индексация, методы  
Списки:Объявление, индексация, методы  
Кортежи:Объявление, индексация, методы  
Множества:Объявление, методы  
Словари:Объявление, индексация, методы 
Работа с файлами:Открытие, чтение, запись, закрытие  
Обработка исключений:try, except, finally, raise  
Модули:Импорт, использование  
ООП в Python:Классы, объекты, наследование, полиморфизм  
Работа с датами:Объект datetime, форматирование даты 
Работа с JSON:Сериализация, десериализация 
Работа с регулярными выражениями:Использование, методы 
Работа с базами данных:SQLite, MySQL, PostgreSQL 
Работа с сетью:Обзор, сокеты, HTTP, FTP 
Работа с многопоточностью:threading, multiprocessing 
Введение в JavaScript:Синтаксис, типы данных, переменные, операторы 
Управляющие конструкции:if, else, switch, циклы 
Функции:Объявление, вызов, аргументы, возвращаемое значение 
Объекты:Объявление, доступ к свойствам, методы, конструкторы  
Массивы:Объявление, доступ к элементам, методы  
Работа с датами: Объект Date, форматирование даты 
Работа с DOM:Получение элементов, изменение свойств, события 
Работа с событиями:Типы событий, обработчики событий  
Асинхронность:Callbacks, Promises, async/await  
Работа с AJAX:Объект XMLHttpRequest, fetch API  
Работа с JSON:Сериализация, десериализация  
Модули: Импорт, экспорт  
ООП в JavaScript:Классы, объекты, наследование, полиморфизм  
Работа с Canvas:Рисование фигур, текста, изображений  
Работа с SVG:Создание фигур, анимация
Введение в HTML и CSS: 
Основы HTML:Структура, теги, атрибуты 
Основы CSS:Синтаксис, селекторы, свойства 
Работа с текстом в HTML и CSS:Текст HTML/CSS 
Работа с изображениями в HTML и CSS:Изображения HTML/CSS  
Работа с ссылками в HTML и CSS:Ссылки HTML/CSS  
Работа с таблицами в HTML и CSS:Таблицы HTML/CSS  
Работа с формами в HTML и CSS:Формам HTML/CSS  
Работа с CSS-свойствами:Цвета, фоны, размеры, позиционирование  
Работа с CSS-свойствами:Блочная модель, отображение, переполнение  
Работа с CSS-свойствами:Псевдоклассы, псевдоэлементы  
Работа с CSS-свойствами:Трансформации, анимации  
Работа с CSS-свойствами:Сетки, флексбокс, гриды  
Работа с CSS-препроцессорами:SASS, LESS
'''
slugs = '''introduction-to-python
control-structures
functions
operators
strings
lists
tuples
sets
dictionaries
working-with-files
exception-handling
modules
oop-in-python
working-with-dates-in-python
working-with-json-in-python
working-with-regular-expressions
working-with-databases
working-with-networking
working-with-multithreading
introduction-to-javascript
control-structures-in-javascript
functions-in-javascript
objects-in-javascript
arrays-in-javascript
working-with-dates-in-javascript
working-with-dom-in-javascript
working-with-events-in-javascript
asynchronous-programming-in-javascript
ajax-work-in-javascript
working-with-json-in-javascript
modules-in-javascript
oop-in-javascript
working-with-canvas-in-javascript
working-with-svg-in-javascript
intro-to-html-and-css
html-basics
css-basics
working-with-text-in-html-and-css
working-with-images-in-html-and-css
working-with-links-in-html-and-css
working-with-tables-in-html-and-css
working-with-forms-in-html-and-css
working-with-css-properties
working-with-css-preprocessors'''
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
                'text': 'hello',
                }

    return render(request, 'codelang/topic-page.html', context=data)

def show_registration_page(request):
    data = {'title': 'Регистрация'}
    return render(request, 'codelang/reg_form.html', context=data)

def authorization(request):
    data = {'title': 'Главная страница'}
    return render(request, 'codelang/index.html', context=data)
