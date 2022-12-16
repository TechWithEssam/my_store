# Generated by Django 4.1.3 on 2022-12-07 23:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_cartitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(70), django.core.validators.MinValueValidator(0)]),
        ),
    ]