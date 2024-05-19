from django.db import models


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

    def __str__(self):
        return f'{self.first_mailing}, статус: {self.status}, периодичность: {self.periodicity}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ('first_mailing', )

