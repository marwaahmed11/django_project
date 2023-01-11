# Generated by Django 4.1.4 on 2023-01-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_employee_relation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='relation',
        ),
        migrations.AddField(
            model_name='employee',
            name='cars',
            field=models.ManyToManyField(to='pages.car'),
        ),
    ]