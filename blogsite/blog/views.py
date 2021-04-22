from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
    posts = Post.objects.filter(status='published')
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
