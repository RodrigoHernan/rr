# Generated by Django 2.0 on 2018-04-20 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('hecho', models.BooleanField()),
                ('descripcion', models.CharField(max_length=400)),
                ('grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tareas.Grupo')),
            ],
        ),
    ]
