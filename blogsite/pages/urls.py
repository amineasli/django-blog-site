from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('about/', views.about_page, name='about_page'),
]   