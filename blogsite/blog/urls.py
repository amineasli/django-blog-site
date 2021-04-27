from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.post_detail,
        name='post_detail'),
    path('tag/<slug:slug>/',
        views.tag_detail,
        name='tag_detail'),
    path('tags/',
        views.tag_list,
        name='tag_list'),
    path('', views.post_index, name='post_index'),
]   