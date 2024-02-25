from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article, Tag


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all()
    context = {'object_list': articles}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    ordering = '-published_at'

    return render(request, template, context)


def tags_add(request):
    tags_list = ['Город','Здоровье','Космос','Культура','Международные отношения','Наука']

    for tag in tags_list:
        Tag.objects.create(name=tag)

    tag_str = ', '.join(tags_list)

    return HttpResponse(f'Список разделов: {tag_str}')