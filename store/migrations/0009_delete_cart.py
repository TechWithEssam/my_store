# Generated by Django 4.1.3 on 2022-12-07 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]