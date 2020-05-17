from django.db import models


class CategoryQuerySet(models.QuerySet):

    def get_slug(self, slug):
        return self.filter(slug=slug)

    def get_name(self, name):
        return self.filter(name=name)

    def get_id(self, id):
        return self.filter(id=id)


class CategoryManager(models.Manager):

    def queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def get_slug(self, slug):
        return self.queryset().get_slug(slug)

    def get_name(self, name):
        return self.queryset().get_name(name)

    def get_id(self, id):
        return self.queryset().get_id(id)


class SubCategoryQuerySet(models.QuerySet):

    def get_slug(self, slug):
        return self.filter(slug=slug)

    def get_name(self, name):
        return self.filter(name=name)

    def get_id(self, id):
        return self.filter(id=id)

    def get_category_id(self, category_id):
        return self.filter(category__id=category_id)


class SubCategoryManager(models.Manager):

    def queryset(self):
        return SubCategoryQuerySet(self.model, using=self._db)

    def get_slug(self, slug):
        return self.queryset().get_slug(slug)

    def get_name(self, name):
        return self.queryset().get_name(name)

    def get_id(self, id):
        return self.queryset().get_id(id)

    def get_category_id(self, category_id):
        return self.queryset().get_category_id(category_id)


class ProjectQuerySet(models.QuerySet):

    def get_slug(self, slug):
        return self.filter(slug=slug)

    def get_name(self, name):
        return self.filter(name=name)

    def get_id(self, id):
        return self.filter(id=id)

    def get_category_id(self, category_id):
        return self.filter(category__id=category_id)

    def get_subcategory_id(self, subcategory_id):
        return self.filter(subcategory__id=subcategory_id)


class ProjectManager(models.Manager):

    def queryset(self):
        return ProjectQuerySet(self.model, using=self._db)

    def get_slug(self, slug):
        return self.queryset().get_slug(slug)

    def get_name(self, name):
        return self.queryset().get_name(name)

    def get_id(self, id):
        return self.queryset().get_id(id)

    def get_category_id(self, category_id):
        return self.queryset().get_category_id(category_id)

    def get_subcategory_id(self, sub_category_id):
        return self.queryset().get_subcategory_id(sub_category_id)
