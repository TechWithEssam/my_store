# Generated by Django 4.1.3 on 2022-12-08 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_is_buyer'),
        ('store', '0022_remove_orderplaced_cart_orderplaced_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]