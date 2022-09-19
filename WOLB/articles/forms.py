from django import forms
from .models import Article


class ArticleForms(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_title', 'article_text', 'photo', 'is_published', 'category']

        widgets = {
            'article_title': forms.TextInput(attrs={'class': 'form-control'}),
            'article_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control', 'labels': 'Категории'}),
        }

# article_title = forms.CharField(max_length=200,
#                                 label='Название',
#                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
#
# article_text = forms.CharField(label="Текст",
#                                required=False,
#                                widget=forms.Textarea(attrs={
#                                    'row': 5,
#                                    'class': 'form-control'}))
#
# is_published = forms.BooleanField(label="Опубликовано?",
#                                   initial=True)
#
# category = forms.ModelChoiceField(queryset=Category.objects.all(),
#                                   label="Категория",
#                                   empty_label='Выберете категорию',
#                                   widget=forms.Select({'class': 'form-control'}))
