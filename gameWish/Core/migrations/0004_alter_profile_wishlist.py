# Generated by Django 5.0 on 2024-01-10 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='wishlist',
            field=models.TextField(blank=True),
        ),
    ]
