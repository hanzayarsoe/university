# Generated by Django 5.0 on 2024-11-28 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_generalinfo_about_us_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='is_popular',
            field=models.BooleanField(default=True),
        ),
    ]