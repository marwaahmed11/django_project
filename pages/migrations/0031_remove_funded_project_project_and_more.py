# Generated by Django 4.1.4 on 2023-01-17 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_project_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funded_project',
            name='project',
        ),
        migrations.RemoveField(
            model_name='funded_project',
            name='user',
        ),
        migrations.AlterField(
            model_name='project',
            name='current_situation',
            field=models.IntegerField(null=True),
        ),
    ]
