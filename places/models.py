from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    short_description = models.TextField(verbose_name='Короткое описание')
    long_description = HTMLField(verbose_name='Длинное описание')
    lng = models.FloatField(
        verbose_name='Долгота',
    )
    lat = models.FloatField(
        verbose_name='Широта',
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        related_name='images',
        verbose_name='Место',
        on_delete=models.CASCADE,
    )
    image = models.ImageField('Изображение')

    position = models.PositiveIntegerField(
        verbose_name='Позиция',
        default=0,
        null=True,
        blank=True,
        db_index=True,
    )

    class Meta:
        ordering = ['position']
