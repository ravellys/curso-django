# Generated by Django 3.1.1 on 2020-09-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='v_id',
            field=models.CharField(default='1 ', max_length=32),
        ),
    ]
