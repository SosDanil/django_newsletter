from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=400, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое статьи')
    preview = models.ImageField(upload_to='blogs/', verbose_name='изображение', blank=True, null=True)
    counts_of_view = models.SmallIntegerField(default=0, verbose_name='количество просмотров')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return f'{self.title}({self.publish_date})'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

