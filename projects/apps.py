from django.apps import AppConfig
from django.conf import settings


class ProjectsConfig(AppConfig):
    name = 'projects'

    def ready(self):
        if settings.MIGRATION_REQUIRED:
            from django.core import management
            management.call_command('migrate')
            management.call_command('loadstructure')
