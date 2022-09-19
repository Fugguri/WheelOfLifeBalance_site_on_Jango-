from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Article, Comment, Category


def index(request):
    articles_list = Article.objects.all()
    categories = Category.objects.all()
    context = {'articles_list': articles_list,
               "title": "Список статей",
               'category': categories,

               }
    return render(request, 'articles/index.html', context)


def article(request, article_id):
    art = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/details.html', {'article': art})


def article_and_comments(request, article_id):
    art = get_object_or_404(Article, pk=article_id)
    comm = get_list_or_404(Comment, article_id=article_id)
    return render(request, 'articles/artncomm.html', {'article': art, 'comm': comm})


def comments(request, article_id):
    comm = get_list_or_404(Comment)
    return render(request, 'articles/details.html', {'art': comm})


def get_categories(request, category_id):
    articles = get_list_or_404(Article, category_id=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {'articles': articles,
               'category': category
               }
    return render(request, 'articles/category.html', context=context)