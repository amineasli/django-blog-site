from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Post

def index(request):
    posts = Post.objects.filter(status='published')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)
