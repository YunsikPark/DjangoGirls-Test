from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Post

def post_list(request):
    # posts = Post.objects.filter(
    #     published_date__lte = timezone.now()
    # )
    posts = Post.objects.all()
    context = {
        'title' : 'PostList from post_list view',
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context=context)

