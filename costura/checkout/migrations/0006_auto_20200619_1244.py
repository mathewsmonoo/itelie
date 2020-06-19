# Generated by Django 3.0.4 on 2020-06-19 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_auto_20200619_1156'),
        ('checkout', '0005_cartitem_sale_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Aguardando Pagamento'), (1, 'Compra Concluída'), (2, 'Compra CANCELADA')], default=0, verbose_name='Situação')),
                ('payment_option', models.CharField(choices=[('pagseguro', 'PagSeguro'), ('paypal', 'Paypal')], max_length=20, verbose_name='Opção de Pagamento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='Preço Promocional(R$)'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='Preço(R$)')),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='Preço Promocional(R$)')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checkout.Order', verbose_name='Pedido')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Item do pedido',
                'verbose_name_plural': 'Itens dos pedidos',
            },
        ),
    ]