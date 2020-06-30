# Generated by Django 3.0.4 on 2020-06-30 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200619_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='Preço Promocional(R$)'),
            preserve_default=False,
        ),
    ]
