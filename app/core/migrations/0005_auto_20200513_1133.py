# Generated by Django 3.0.5 on 2020-05-13 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time_miniutes',
            new_name='time_minutes',
        ),
    ]
