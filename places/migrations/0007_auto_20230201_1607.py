# Generated by Django 3.2.16 on 2023-02-01 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_detailsurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='placeId',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
    ]