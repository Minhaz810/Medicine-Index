# Generated by Django 5.1.2 on 2024-10-28 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufacturer',
            old_name='descrtiption',
            new_name='description',
        ),
    ]
