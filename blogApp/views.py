from django.shortcuts import render, get_object_or_404
from .models import Post

def home_page(request):
    posts = Post.objects.all().order_by('-post_date')[:4]
    context = {
        'posts': posts
    }
    return render(request, "./index.html", context)

def all_news_page(request):
    posts = Post.objects.all().order_by('-post_date')
    context = {
        'posts': posts
    }
    return render(request, "./news-list.html", context)

def news_detail_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, "./news-detail.html", context)
