# Generated by Django 3.0.4 on 2020-09-13 03:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200912_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_nickname', models.CharField(blank=True, default='', max_length=25, verbose_name='Nick')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('staff_number', models.PositiveIntegerField(blank=True)),
                ('department', models.CharField(blank=True, default='', max_length=9, verbose_name='Setor')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Administrador'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Equipe'),
        ),
    ]