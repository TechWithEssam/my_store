# Generated by Django 4.1.3 on 2022-12-08 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_rename_country_orderplaced_state_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='state',
        ),
    ]