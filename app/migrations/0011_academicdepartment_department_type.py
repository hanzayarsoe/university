# Generated by Django 5.0 on 2024-11-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_imageshowcase'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicdepartment',
            name='department_type',
            field=models.CharField(default='academic', max_length=50),
        ),
    ]
