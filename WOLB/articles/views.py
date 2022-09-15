from django.http import HttpResponse
from .models import Article, Comment
from django.template import loader
from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.http import Http404


def index(request):
    articles_list = Article.objects.all()
    context = {'articles_list': articles_list,
               "title" : "Список статей"}
    return render(request, 'articles/index.html', context)


def article(request, article_id):
    art = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/details.html', {'art': art})


def article_and_comments(request, article_id):
    art = get_object_or_404(Article, pk=article_id)
    comm = get_list_or_404(Comment, article_id=article_id)
    return render(request, 'articles/artncomm.html', {'art': art, 'comm': comm})


def comments(request, article_id):
    comm = get_list_or_404(Comment)
    return render(request, 'articles/details.html', {'art': comm})


