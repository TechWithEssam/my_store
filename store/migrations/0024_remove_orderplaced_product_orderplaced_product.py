# Generated by Django 4.1.3 on 2022-12-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_alter_orderplaced_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='product',
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='product',
            field=models.ManyToManyField(to='store.product'),
        ),
    ]
