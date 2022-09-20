from django import template
from ..models import Category, Comment

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_list_categories():
    return Category.objects.all()


@register.inclusion_tag('articles/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}


@register.simple_tag(name='get_all_comments')
def get_all_comments():
    return Comment.objects.all()