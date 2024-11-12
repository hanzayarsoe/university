# Generated by Django 5.0 on 2024-11-10 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_course_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='credits',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]