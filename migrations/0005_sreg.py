# Generated by Django 4.0.3 on 2022-04-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_delete_registeredforms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
            ],
            options={
                'db_table': 'reg',
            },
        ),
    ]
