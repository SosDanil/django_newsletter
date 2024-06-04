from django.db import models

from clients.models import Client
from text_messages.models import TextMessage
from users.models import User


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
    last_mailing = models.DateTimeField(verbose_name='Время и дата последней отправки')
    status = models.CharField(max_length=9, choices=STATUSES, default=CREATED, verbose_name='статус рассылки')
    periodicity = models.CharField(max_length=20, choices=PERIODICITY, verbose_name='Периодичность рассылки')

    is_active = models.BooleanField(verbose_name='рассылка активна', default=True)

    message = models.ForeignKey(TextMessage, on_delete=models.CASCADE, verbose_name='Сообщение')
    to_client = models.ManyToManyField(Client, verbose_name='Клиенту')
    owner = models.ForeignKey(User, verbose_name='Владелец', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return (f'{self.message}, {self.first_mailing}, {self.last_mailing}, статус: {self.status},'
                f' периодичность: {self.periodicity}')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ('first_mailing', )

        permissions = [
            ('set_active', 'Can activate/deactivate newsletter'),
        ]


class TryMailing(models.Model):
    SUCCESS = 'success'
    FAIL = 'fail'

    STATUSES = (
        (SUCCESS, 'успешно'),
        (FAIL, 'не успешно'),
    )

    last_try = models.DateTimeField(verbose_name='Дата и время последней попытки')
    status = models.CharField(max_length=10, choices=STATUSES, verbose_name='статус попытки')
    server_respond = models.TextField(verbose_name='Ответ почтового сервера', null=True, blank=True)

    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, verbose_name='Рассылка')

    def __str__(self):
        return f'{self.last_try}, статус: {self.status}'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
        ordering = ('last_try', )
