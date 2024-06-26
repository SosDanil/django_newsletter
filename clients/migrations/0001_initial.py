# Generated by Django 5.0.6 on 2024-05-19 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='Ф.И.О.')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('gender', models.CharField(choices=[('female', 'женщина'), ('male', 'мужчина')], max_length=10, verbose_name='Пол клиента')),
                ('age', models.SmallIntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ('full_name',),
            },
        ),
    ]
