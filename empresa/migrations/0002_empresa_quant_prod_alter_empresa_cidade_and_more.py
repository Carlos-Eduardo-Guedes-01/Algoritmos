# Generated by Django 4.2 on 2023-05-03 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='quant_prod',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cidade',
            field=models.ForeignKey(default='Informe a Cidade', on_delete=django.db.models.deletion.CASCADE, to='empresa.cidade'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='tipo',
            field=models.ForeignKey(default='Informe o Tipo', on_delete=django.db.models.deletion.CASCADE, to='empresa.tipos'),
        ),
        migrations.AlterField(
            model_name='tipos',
            name='nome_tipo',
            field=models.CharField(default='Selecione o Tipo', max_length=50),
        ),
    ]
