from django.db import models
from django.urls import reverse


class Article(models.Model):
    article_title = models.CharField(verbose_name='Название статьи', max_length=200)
    article_text = models.TextField( blank=True, verbose_name='Текст статьи')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    redact_date = models.DateTimeField(auto_now=True, verbose_name="Отредактировано")
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, verbose_name="Категории")

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_id': self.pk})

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"
    # ordering = ["-pub_date"]


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)

    def get_absolute_url(self):
        return reverse('comments', kwargs={'pk': self.pk})

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['article']


class Category(models.Model):
    title = models.CharField(max_length=70, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('categories', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
