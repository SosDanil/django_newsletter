from django.db import models

from django.db import models


class TextMessage(models.Model):
    subject = models.CharField(max_length=300, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма', blank=True, null=True)

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

