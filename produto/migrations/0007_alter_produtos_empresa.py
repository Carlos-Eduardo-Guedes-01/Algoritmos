# Generated by Django 4.2 on 2023-05-08 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_alter_empresa_quant_prod'),
        ('produto', '0006_alter_produtos_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='empresa',
            field=models.ForeignKey(default='Informe o estabelecimento', null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
    ]