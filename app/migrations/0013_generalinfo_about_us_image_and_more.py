# Generated by Django 5.0 on 2024-11-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_managementdepartment_department_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='about_us_image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='about_us',
            field=models.TextField(blank=True, default='About University', null=True),
        ),
    ]
