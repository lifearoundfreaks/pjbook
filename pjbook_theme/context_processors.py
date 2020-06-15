from projects.models import Category


def default(self):
    return {"category_data": Category.objects.values_list('name', 'slug')}
