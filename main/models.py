from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse_lazy


class News(models.Model):
    header = models.CharField(verbose_name='Заголовок', max_length=250)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
    annotation = models.TextField(verbose_name='Аннотация')
    text = models.TextField(verbose_name='Текст статьи')
    date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    author = models.ForeignKey('Author', verbose_name='Автор', blank=True, null=True,  on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='media/img/news_img/%Y/%m/%d/')
    photo_url = models.CharField(verbose_name='URL изображения', max_length=250, blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy('news_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Author(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    surname = models.CharField(verbose_name='Фамилия', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Comment(models.Model):
    news = models.ForeignKey('News', verbose_name='Новость',  on_delete=models.CASCADE)
    username = models.OneToOneField(User, verbose_name='Имя пользователя', on_delete=models.CASCADE, primary_key=True,)
    comment_date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    comment = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Category(models.Model):
    category_name = models.CharField(verbose_name='Категория', max_length=20)

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

