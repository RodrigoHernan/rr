# Generated by Django 2.0 on 2018-04-20 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0003_auto_20180420_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
