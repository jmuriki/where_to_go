# Generated by Django 3.2.16 on 2023-02-01 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_place_placeid'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='detailsUrl',
            field=models.URLField(default='detailsUrl', verbose_name='detailsUrl'),
            preserve_default=False,
        ),
    ]
