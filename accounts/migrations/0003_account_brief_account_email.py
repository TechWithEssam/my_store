# Generated by Django 4.1.3 on 2022-12-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_account_captcha_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='Brief',
            field=models.TextField(default='hi'),
        ),
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]