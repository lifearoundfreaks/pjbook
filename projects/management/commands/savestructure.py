from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import Subcategory

import json
import os


class Command(BaseCommand):
    help = 'Saves current category structure as a json file'

    def handle(self, *args, **options):
        path = os.path.join(settings.SITE_ROOT, "structure.json")

        try:
            with open(path, 'r') as _file:
                current_version = json.load(_file)['version']
        except FileNotFoundError:
            current_version = 0

        data = {'categories': {}, 'version': current_version+1}
        for category, category_name, slug, name in \
            Subcategory.objects.values_list(
                'category__slug', 'category__name', 'slug', 'name'):
            if category not in data['categories']:
                data['categories'][category] = {
                    'name': category_name, 'subcategories': {}}
            data['categories'][category]['subcategories'][slug] = \
                {"name": name}

        with open(path, 'w') as _file:
            _file.write(json.dumps(data, indent=4))
