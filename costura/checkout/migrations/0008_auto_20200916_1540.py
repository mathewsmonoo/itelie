# Generated by Django 3.0.4 on 2020-09-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20200619_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Preço Promocional(R$)'),
        ),
    ]
