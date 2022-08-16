from django.shortcuts import render
from .models import News


def blog(request):
    news = News.objects.all()

    context = {
        'news': news,
    }
    return render(request, 'news/blog.html', context=context)
