# Generated by Django 4.1.3 on 2022-12-07 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]
