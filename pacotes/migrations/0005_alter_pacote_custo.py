# Generated by Django 4.2 on 2023-06-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0004_pacote_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacote',
            name='custo',
            field=models.CharField(max_length=10, verbose_name='Custo do Pacote'),
        ),
    ]