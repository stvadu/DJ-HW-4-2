from django.urls import path

from articles.views import articles_list, tags_add

urlpatterns = [
    path('', articles_list, name='articles'),
    path('tags_add/', tags_add, name='tags'),
]