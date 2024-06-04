from django.db import models

from users.models import User


class Client(models.Model):
    FEMALE = 'female'
    MALE = 'male'

    GENDERS = (
        (FEMALE, 'женщина'),
        (MALE, 'мужчина'),
    )

    full_name = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    email = models.EmailField(verbose_name='Почта', unique=True)
    gender = models.CharField(max_length=10, choices=GENDERS, verbose_name='Пол клиента')
    age = models.SmallIntegerField(verbose_name='Возраст', null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)

    owner = models.ForeignKey(User, verbose_name='Владелец', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.full_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('full_name', )
