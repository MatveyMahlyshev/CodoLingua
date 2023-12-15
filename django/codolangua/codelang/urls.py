from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('python/', views.show_python_page, name='python'),
    path('js/', views.show_js_page, name='js'),
    path('html-css/', views.show_html_css_page, name='html-css'),
    path('python/<slug:python_slug>/', views.show_topic_page, name='python_topic'),
    path('registration/', views.show_registration_page, name='registration'),
]