# Generated by Django 5.0 on 2024-11-10 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_category_options_alter_coursecategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='img_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
