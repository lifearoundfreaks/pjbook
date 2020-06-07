# Generated by Django 3.0.2 on 2020-05-19 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('projects', '0001_initial'), ('projects', '0002_auto_20200517_1626'), ('projects', '0003_auto_20200517_1627')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Category')),
            ],
            options={
                'verbose_name_plural': 'subcategories',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Category')),
                ('subcategory', models.ManyToManyField(to='projects.SubCategory')),
            ],
            options={
                'verbose_name_plural': 'projects',
            },
        ),
    ]