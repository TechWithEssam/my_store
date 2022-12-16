# Generated by Django 4.1.3 on 2022-12-08 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_is_buyer'),
        ('store', '0013_rating_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('town', models.CharField(blank=True, max_length=100, null=True, verbose_name='Town/City')),
                ('county', models.CharField(blank=True, max_length=100, null=True, verbose_name='County')),
                ('post_code', models.CharField(blank=True, max_length=8, null=True, verbose_name='Post Code')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country')),
                ('longitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude')),
                ('latitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
