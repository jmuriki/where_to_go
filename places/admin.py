from django.contrib import admin
from django.utils.html import format_html
from places.models import Place, Image
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableTabularInline


class ImageInline(SortableTabularInline):
    model = Image

    fields = [
        'image',
        'show_image_preview',
        'position',
    ]

    readonly_fields = ['show_image_preview']

    def show_image_preview(self, object):
        return format_html(
            '<img src="{url}" height="200px"/>',
            url=object.image.url,
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ['title']

    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        'place',
        'image',
        'show_image_preview',
    ]

    readonly_fields = ['show_image_preview']

    def show_image_preview(self, object):
        return format_html(
            '<img src="{url}" height="200px"/>',
            url=object.image.url,
        )
