# Generated by Django 4.1.3 on 2022-12-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
