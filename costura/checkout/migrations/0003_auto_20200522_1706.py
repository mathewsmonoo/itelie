# Generated by Django 3.0.4 on 2020-05-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200522_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=99, max_digits=8, verbose_name='Preço(R$)'),
            preserve_default=False,
        ),
    ]