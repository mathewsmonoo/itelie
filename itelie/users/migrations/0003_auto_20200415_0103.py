# Generated by Django 3.0.4 on 2020-04-15 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200415_0103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='addressess',
            new_name='addresses',
        ),
    ]
