from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.post_detail,
        name='post-detail'),
    path('', views.post_index, name='post-index'),
]   