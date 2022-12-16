# Generated by Django 4.1.3 on 2022-12-14 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_orderplaced_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_order', models.IntegerField(default=1)),
                ('first_name_order', models.CharField(blank=True, max_length=120, null=True)),
                ('last_name_order', models.CharField(blank=True, max_length=120, null=True)),
                ('email_order', models.EmailField(blank=True, max_length=60, null=True)),
                ('address_order', models.CharField(blank=True, max_length=100, null=True)),
                ('address2_order', models.CharField(blank=True, max_length=120, null=True)),
                ('country_order', models.CharField(blank=True, max_length=100, null=True)),
                ('state_order', models.CharField(blank=True, max_length=200, null=True)),
                ('zip_code_order', models.CharField(blank=True, max_length=10, null=True)),
                ('timestamp_order', models.DateTimeField(auto_now_add=True)),
                ('updated_order', models.DateTimeField(auto_now=True)),
                ('status_order', models.CharField(blank=True, max_length=20, null=True)),
                ('orders', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.orderplaced')),
            ],
        ),
    ]
