# Generated by Django 4.2 on 2023-06-13 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0006_pacote_quant_carousel'),
        ('empresa', '0005_alter_empresa_cidade_alter_empresa_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='pacote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pacotes.pacote', verbose_name='Selecione o Pacote'),
        ),
    ]