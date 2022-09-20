from django.shortcuts import render, get_object_or_404, get_list_or_404,redirect
from .forms import ArticleForms
from .models import Article, Comment, Category
from django.views.generic import ListView, DetailView, CreateView


class HomeArticle(ListView):
    model = Article
    template_name = 'articles/home_article_list.html'
    context_object_name = 'articles'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticlesByCategory(ListView):
    model = Article
    template_name = 'articles/home_article_list.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewArticle(DetailView):
    model = Article
    template_name = 'articles/artncomm.html'

    # pk_url_kwarg = 'article_id'
    # template_name = 'article/article_detail.html'


class CreateArticle(CreateView):
    form_class = ArticleForms
    template_name = 'articles/add_article.html'




#
# def index(request):
#     articles_list = Article.objects.all()
#     categories = Category.objects.all()
#     context = {'articles_list': articles_list,
#                "title": "Список статей",
#                'category': categories,
#
#                }
#     return render(request, 'articles/index.html', context)


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


def add_article(request):
    if request.method == "POST":
        form = ArticleForms(request.POST)
        if form.is_valid():
            Article.objects.create(**form.cleaned_data)
            articles = form.save()
            return redirect(articles)
            # article = Article.objects.create(**form.cleaned_data)
            # redirect may go us to article redirect (article)
    else :
        form = ArticleForms()
    return render(request, 'articles/add_article.html', {'form': form })
