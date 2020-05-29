from django.db import models


class ProjectQuerySet(models.QuerySet):

    def get_category_by_id(self, category_id):
        return self.filter(category__id=category_id)

    def get_subcategory_by_id(self, subcategory__id):
        return self.filter(subcategory__id=subcategory__id)


class ProjectManager(models.Manager):

    def queryset(self):
        return ProjectQuerySet(self.model, using=self._db)

    def get_category_by_id(self, category_id):
        return self.queryset().get_category_by_id(category_id)

    def get_subcategory_by_id(self, sub_category_id):
        return self.queryset().get_subcategory_by_id(sub_category_id)
