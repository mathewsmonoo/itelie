# Generated by Django 3.0.4 on 2020-09-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20200916_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prefix',
            field=models.CharField(blank=True, max_length=8, verbose_name='Prefixo / Apelido'),
        ),
    ]