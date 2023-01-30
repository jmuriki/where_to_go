from django.contrib import admin
from places.models import Place, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
        list_display = [
        'image',
    ]
