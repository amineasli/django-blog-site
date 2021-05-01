from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Tag
from .forms import CommentForm

def post_index(request):
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
    return render(request, 'blog/post_index.html', context)

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)


    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    context = { 'post': post,
                'comments': comments,
                'new_comment': new_comment,
                'comment_form': comment_form,
    }

    return render(request, 'blog/post_detail.html', context)

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    context = {'posts': tag.posts.all(), 'tag': tag.name}
    return render(request, 'blog/tag_detail.html', context)
