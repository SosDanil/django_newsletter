from django.db import models

from clients.models import Client
from messages.models import Message


class Newsletter(models.Model):
    CREATED = 'created'
    LAUNCHED = 'launched'
    COMPLETED = 'completed'

    STATUSES = (
        (CREATED, 'Создана'),
        (LAUNCHED, 'Запущена'),
        (COMPLETED, 'Завершена'),
    )

    ONCE_A_DAY = 'every day'
    ONCE_A_WEEK = 'every week'
    ONCE_A_MONTH = 'every month'

    PERIODICITY = (
        (ONCE_A_DAY, 'Раз в день'),
        (ONCE_A_WEEK, 'Раз в неделю'),
        (ONCE_A_MONTH, 'Раз в месяц'),
    )

    first_mailing = models.DateTimeField(verbose_name='Время и дата первой отправки')
    status = models.CharField(max_length=9, choices=STATUSES, default=CREATED, verbose_name='статус рассылки')
    periodicity = models.CharField(max_length=11, choices=PERIODICITY, verbose_name='Периодичность рассылки')

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    to_client = models.ManyToManyField(Client, verbose_name='Клиенту')

    def __str__(self):
        return f'{self.first_mailing}, статус: {self.status}, периодичность: {self.periodicity}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ('first_mailing', )


class TryMailing(models.Model):
    SUCCESS = 'success'
    FAIL = 'fail'

    STATUSES = (
        (SUCCESS, 'успешно'),
        (FAIL, 'не успешно'),
    )

    last_try = models.DateTimeField(verbose_name='Дата и время последней попытки')
    status = models.CharField(max_length='7', choices=STATUSES, verbose_name='статус попытки')
    server_respond = models.TextField(verbose_name='Ответ почтового сервера', null=True, blank=True)

    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name='Рассылка')

    def __str__(self):
        return f'{self.last_try}, статус: {self.status}'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
        ordering = ('last_try', )
