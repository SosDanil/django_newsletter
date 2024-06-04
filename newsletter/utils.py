import smtplib

from django.core.mail import send_mail

from config.settings import TIME_ZONE, EMAIL_HOST_USER
import pytz
from datetime import datetime

from newsletter.models import Newsletter, TryMailing

MY_TIME_ZONE = pytz.timezone(TIME_ZONE)
NOW = datetime.now(MY_TIME_ZONE)


def send_mail_func(newsletter):
    """Отправляет письмо на почту клиентам из рассылки, записывает попытки рассылки"""
    client_emails = newsletter.to_client.values_list('email', flat=True)
    subject = newsletter.message.subject
    text_of_message = newsletter.message.body
    try:
        send_response = send_mail(
            subject=subject,
            message=text_of_message,
            from_email=EMAIL_HOST_USER,
            recipient_list=client_emails,
            fail_silently=False,
        )
        TryMailing.objects.create(last_try=NOW, status=TryMailing.SUCCESS, server_respond=send_response,
                                  newsletter=newsletter)
        return send_response
    except smtplib.SMTPException as e:
        TryMailing.objects.create(last_try=NOW, status=TryMailing.FAIL, server_respond=e,
                                  newsletter=newsletter)


def launch_newsletter():
    """Запускает рассылки, меняет их статусы, проверяет периодичность"""
    newsletters = (Newsletter.objects.filter(status__in=['created', 'launched']).filter(first_mailing__lte=NOW).
                   prefetch_related('to_client').select_related('message'))

    for newsletter in newsletters:
        print('прошел по рассылке')
        if not newsletter.is_active:
            print('рассылка отключена')
            continue
        else:
            if newsletter.last_mailing < NOW:
                newsletter.status = newsletter.COMPLETED
                newsletter.save()
                print('отработал статус COMPLETED')

            elif newsletter.status == newsletter.CREATED:
                send_mail_func(newsletter)
                newsletter.status = newsletter.LAUNCHED
                newsletter.save()
                print('Отработала отправка и смена статуса на ЗАПУЩЕНО')

            elif newsletter.status == newsletter.LAUNCHED:
                last_try = TryMailing.objects.filter(newsletter=newsletter).order_by('-last_try').first()
                delta = NOW - last_try.last_try
                if newsletter.periodicity == newsletter.ONCE_A_DAY and delta.days >= 1:
                    send_mail_func(newsletter)
                    print('Отработала отправка рассылки со статусом Запущена каждый день')
                elif newsletter.periodicity == newsletter.ONCE_A_WEEK and delta.days >= 7:
                    send_mail_func(newsletter)
                    print('Отработала отправка рассылки со статусом Запущена каждую неделю')
                elif newsletter.periodicity == newsletter.ONCE_A_MONTH and delta.days >= 30:
                    send_mail_func(newsletter)
                    print('Отработала отправка рассылки со статусом Запущена каждый месяц')

    print(f'Текущее время:{NOW}')
