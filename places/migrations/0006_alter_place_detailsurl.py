# Generated by Django 3.2.16 on 2023-02-01 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_place_detailsurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='detailsUrl',
            field=models.CharField(max_length=200, verbose_name='detailsUrl'),
        ),
    ]
