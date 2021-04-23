from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

def index(request):
    posts = Post.objects.filter(status='published')
    paginator = Paginator(posts, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
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
