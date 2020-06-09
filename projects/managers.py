from django.db.models import Manager, QuerySet, Count


class ProjectQueryset(QuerySet):
    def with_subcategories(self, subcategory_slugs):
        return self.filter(subcategories__slug__in=subcategory_slugs)

    def with_all_subcategories(self, subcategory_slugs):
        return self.with_subcategories(subcategory_slugs).annotate(
            num_attr=Count('id')).filter(num_attr=len(subcategory_slugs))


class ProjectManager(Manager):
    def get_queryset(self):
        return ProjectQueryset(self.model, using=self._db)

    def with_subcategories(self, subcategory_slugs):
        return self.with_subcategories().authors()

    def with_all_subcategories(self, subcategory_slugs):
        return self.with_all_subcategories().authors()
