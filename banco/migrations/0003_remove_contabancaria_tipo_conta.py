# Generated by Django 4.1 on 2022-08-10 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0002_remove_usuario_posui_cnpj_contabancaria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contabancaria',
            name='Tipo_Conta',
        ),
    ]
