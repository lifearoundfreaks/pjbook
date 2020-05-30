# Generated by Django 3.0.6 on 2020-05-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_squashed_0003_auto_20200517_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='subcategory',
            field=models.ManyToManyField(to='projects.Subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
