from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import Category, Subcategory

import json
import os


class Command(BaseCommand):
    help = 'Loads saved structure into the database'

    def handle(self, *args, **options):
        path = os.path.join(settings.SITE_ROOT, "structure.json")

        current_categories = Category.objects.in_bulk(field_name='slug')
        current_subcategories = Subcategory.objects.in_bulk(
            field_name='slug')

        with open(path, 'r') as _file:
            data = json.load(_file)
            current_categories = Category.objects.prefetch_related(
                'subcategory_set').in_bulk(field_name='slug')
            current_subcategories = {
                subcategory.slug: subcategory for category in
                current_categories.values() for subcategory in
                category.subcategory_set.all()}

            print("Deleting current categories: ", end='')
            Category.objects.all().delete()
            print("DELETED")

            subcategories, to_save = {}, []
            for slug, category in data['categories'].items():
                # Collecting subcategories for later
                for sub_slug, subcategory in category['subcategories'].items():
                    subcategories[sub_slug] = {**subcategory, 'category': slug}

                upd_category = current_categories.get(
                    slug, Category(slug=slug))
                for key, value in category.items():
                    setattr(upd_category, key, value)
                to_save.append(upd_category)

            print("Adding updated categories: ", end='')
            Category.objects.bulk_create(to_save)
            print("ADDED")

            print("Deleting current subcategories: ", end='')
            Subcategory.objects.all().delete()
            print("DELETED")

            # Getting updated category ids from db
            get_id = dict(Category.objects.values_list('slug', 'id')).get

            to_save = []
            for slug, subcategory in subcategories.items():
                data = subcategory.copy()
                data['category_id'] = get_id(data.pop('category'))
                upd_sub = current_subcategories.get(
                    slug, Subcategory(slug=slug))
                for key, value in data.items():
                    setattr(upd_sub, key, value)
                to_save.append(upd_sub)

            print("Adding updated subcategories: ", end='')
            Subcategory.objects.bulk_create(to_save)
            print("ADDED")
