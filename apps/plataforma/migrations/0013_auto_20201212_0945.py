# Generated by Django 3.1.4 on 2020-12-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0012_auto_20201212_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='seccion',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]