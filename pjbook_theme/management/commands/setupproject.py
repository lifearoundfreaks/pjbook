from django.core.management.base import BaseCommand
from pjbook.utils import setup_project


class Command(BaseCommand):
    help = 'Saves current category structure as a json file'

    def handle(self, *args, **options):
        setup_project(force=True)
