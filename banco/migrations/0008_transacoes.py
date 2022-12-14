# Generated by Django 4.1 on 2022-08-11 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0007_rename_numero_conta_contabancaria_numero_conta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_transferencia', models.DecimalField(decimal_places=2, max_digits=19)),
                ('idUsuario_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Destino', to='banco.usuario')),
                ('idUsuario_origem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Origem', to='banco.usuario')),
            ],
        ),
    ]
