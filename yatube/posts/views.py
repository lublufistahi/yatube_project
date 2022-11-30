from django.shortcuts import render
from .models import Post, Group


# Create your views here.
def group_posts(request, slug):
    template = "posts/group_list.html"
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {'title':title}
    return render(request, template, context)

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Это главная страница проекта Yatube'
    context = {'posts': posts,
               'title':title}
    return render(request, 'posts/index.html', context) 
