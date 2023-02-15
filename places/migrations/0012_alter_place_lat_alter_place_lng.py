# Generated by Django 4.1 on 2023-02-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_alter_place_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.FloatField(default=0, verbose_name='Широта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.FloatField(default=0, verbose_name='Долгота'),
            preserve_default=False,
        ),
    ]