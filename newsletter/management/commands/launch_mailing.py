from django.core.management import BaseCommand

from newsletter.utils import launch_newsletter


class Command(BaseCommand):
    def handle(self, *args, **options):
        launch_newsletter()
