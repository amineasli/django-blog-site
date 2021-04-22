from django.urls import path

from . import views

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.detail,
        name='detail'),
    path('', views.index, name='index'),
]   