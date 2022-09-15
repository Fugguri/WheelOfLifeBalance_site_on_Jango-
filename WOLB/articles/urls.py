from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:article_id>/', views.article, name='article'),
    path('article_and_comments/<int:article_id>/', views.article_and_comments, name='article and comments'),
    path('comments/<int:article_id>/', views.comments, name='comments'),
    ]
