from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('articleandcomments/<int:article_id>/', views.article_and_comments, name='article and comments'),
    path('comments/<int:article_id>/', views.comments, name='comments'),
    path('category/<int:category_id>/', views.get_categories, name='categories'),
    path('article/add/', views.add_article, name='add_article'),
    ]
