# Generated by Django 3.1.2 on 2020-10-13 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.usuario')),
            ],
        ),
    ]