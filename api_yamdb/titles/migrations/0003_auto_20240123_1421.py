# Generated by Django 3.2 on 2024-01-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0002_titlesmodel_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titlesmodel',
            name='genres',
        ),
        migrations.AddField(
            model_name='titlesmodel',
            name='genre',
            field=models.ManyToManyField(
                related_name='genres',
                to='titles.GenresModel',
                verbose_name='Жанры произведения',
            ),
        ),
    ]