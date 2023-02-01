from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    placeId = models.CharField('placeId', max_length=200)
    detailsUrl = models.CharField('detailsUrl', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Длинное описание')
    coordinates_lng = models.FloatField('Долгота', blank=True)
    coordinates_lat = models.FloatField('Широта', blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Изображение', null=True, blank=True)
    place = models.ForeignKey(Place, related_name="images", on_delete=models.CASCADE)


