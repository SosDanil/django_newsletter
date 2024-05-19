from django.db import models


class Message(models.Model):
    subject = models.CharField(max_length=300, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма', blank=True, null=True)

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
