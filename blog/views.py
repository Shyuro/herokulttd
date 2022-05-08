from django.shortcuts import render
from blog.models import Post, Image
from django.conf import settings

# Create your views here.


def post(request, post_id):
    post_n = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post_n})

def slide(request):
    posts = Post.objects.all()
    data = Image.objects.all()
    context = {
        'data' : data,
        'posts': posts
    }
    return render(request, "home.html", context)