# Generated by Django 2.1.1 on 2019-04-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_expediente_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='estado',
            field=models.BooleanField(blank=True, null=True, verbose_name='Estado'),
        ),
    ]