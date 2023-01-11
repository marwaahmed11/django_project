# Generated by Django 4.1.4 on 2023-01-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_project_current_situation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.AddField(
            model_name='project',
            name='target',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]