# Generated by Django 3.0.4 on 2020-04-15 04:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={},
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address_line_2',
            new_name='extra_data',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address_line_1',
            new_name='neighborhood',
        ),
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.RemoveField(
            model_name='address',
            name='name',
        ),
        migrations.AddField(
            model_name='address',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='address',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='address',
            name='number',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='receiver_name',
            field=models.CharField(blank=True, help_text='Nome do destinatário', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='receiver_phone',
            field=models.CharField(blank=True, help_text='Telefone do destinatário', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.CharField(default='Rua', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addressinfo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='address',
            name='nickname',
            field=models.CharField(blank=True, default='nickname', help_text='Apelido do Endereço(ex:Casa da Praia)', max_length=255),
            preserve_default=False,
        ),
    ]