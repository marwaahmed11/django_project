# Generated by Django 4.1.4 on 2023-01-03 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_employee_relation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='relation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.car'),
        ),
    ]
