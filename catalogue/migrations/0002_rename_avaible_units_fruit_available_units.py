# Generated by Django 5.0.4 on 2024-04-08 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fruit',
            old_name='avaible_units',
            new_name='available_units',
        ),
    ]