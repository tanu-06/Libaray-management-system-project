# Generated by Django 4.0.3 on 2022-04-06 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='data',
            new_name='RegisteredForms',
        ),
    ]
