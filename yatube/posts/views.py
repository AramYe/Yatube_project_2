from django.shortcuts import render
# posts/views.py
from django.http import HttpResponse
# Импортируем модель, чтобы обратиться к ней
from .models import Post

def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

def group_posts(request, slug):
    template = 'group.html'
    title = 'Yatube'
    context = {
        'title': title,

        'text': 'Here lies information about the group projects of Yatube'
    }
    return render(request, template, context) 



