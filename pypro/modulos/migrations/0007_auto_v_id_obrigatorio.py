# Generated by Django 3.1.1 on 2020-09-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_aula_v_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='v_id',
            field=models.CharField(max_length=32),
        ),
    ]