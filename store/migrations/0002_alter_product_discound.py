# Generated by Django 4.1.3 on 2022-12-06 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discound',
            field=models.PositiveIntegerField(blank=True, max_length=2, null=True),
        ),
    ]
