# Generated by Django 4.1 on 2022-08-11 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0008_transacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacoes',
            name='idUsuario_destino',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transacoes',
            name='idUsuario_origem',
            field=models.IntegerField(),
        ),
    ]