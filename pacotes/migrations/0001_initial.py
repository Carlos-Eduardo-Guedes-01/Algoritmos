# Generated by Django 4.2.2 on 2023-06-15 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('custo', models.FloatField()),
                ('quant_prod', models.IntegerField()),
            ],
        ),
    ]
