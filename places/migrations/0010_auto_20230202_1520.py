# Generated by Django 3.2.16 on 2023-02-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_remove_place_detailsurl'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='Позиция'),
        ),
    ]