from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', HomeArticle.as_view(), name='index'),
    path('article/<int:pk>/', ViewArticle.as_view(), name='article'),
    # path('articleandcomments/<int:article_id>/', views.article_and_comments, name='article and comments'),
    path('articleandcomments/<int:pk>/', ViewArticle.as_view(), name='article and comments'),
    path('comments/<int:article_id>/', views.comments, name='comments'),
    path('category/<int:category_id>/', ArticlesByCategory.as_view(extra_context={'title': 'text'}),
         name='categories'),
    # path('article/add/', views.add_article, name='add_article'),
    path('article/add/', CreateArticle.as_view(), name='add_article'),

]
