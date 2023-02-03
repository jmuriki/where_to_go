from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Длинное описание')
    coordinates_lng = models.FloatField(
        verbose_name='Долгота',
        null=True,
        blank=True,
    )
    coordinates_lat = models.FloatField(
        verbose_name='Широта',
        null=True,
        blank=True,
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
        null=False,
        blank=False,
        db_index=True,
    )

    class Meta:
        ordering = ['position']
