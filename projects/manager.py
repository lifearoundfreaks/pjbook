from django.db import models


class QuerySet(models.QuerySet):

    def get_category_id(self, category_id):
        return self.filter(category__id=category_id)

    def get_subcategory_id(self, subcategory__id):
        return self.filter(subcategory__id=subcategory__id)


class Manager(models.Manager):

    def queryset(self):
        return QuerySet(self.model, using=self._db)

    def get_category_id(self, category_id):
        return self.queryset().get_category_id(category_id)

    def get_subcategory_id(self, sub_category_id):
        return self.queryset().get_subcategory_id(sub_category_id)
