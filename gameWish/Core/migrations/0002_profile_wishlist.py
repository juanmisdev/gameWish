# Generated by Django 5.0 on 2023-12-27 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='wishlist',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]