import os
import json
import requests

from pathlib import Path
from urllib.parse import unquote
from urllib.parse import urlparse

from places.models import Place, Image
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand


def get_filename_from_url(url):
    url_part = urlparse(url).path
    unquoted_url_part = unquote(url_part)
    filename = os.path.split(unquoted_url_part)[-1]
    return filename


def load_places(folder):
    json_files_paths = [
        os.path.join(folder, filename) for filename in os.listdir(folder)
        if filename.endswith(".json")
    ]
    places_jsons = []
    for path in json_files_paths:
        with open(Path(path), 'r') as json_file:
            places_jsons.append(json.load(json_file))
    for place_json in places_jsons:
        place, _ = Place.objects.get_or_create(
            title=place_json['title'],
            defaults={
                "short_description": place_json['description_short'],
                "long_description": place_json['description_long'],
                "lng": place_json['coordinates']['lng'],
                "lat": place_json['coordinates']['lat'],
            },
        )
        for img_url in place_json['imgs']:
            response = requests.get(img_url)
            response.raise_for_status()
            content = ContentFile(response.content)
            img_name = get_filename_from_url(img_url)
            image_object = Image.objects.create(place=place)
            image_object.image.save(name=img_name, content=content, save=True)


class Command(BaseCommand):

    help = 'Add path to json files folder & images folder'

    def add_arguments(self, parser):
        parser.add_argument(
            '-j',
            '--json_folder',
            required=True,
        )

    def handle(self, *args, **options):
        load_places(options['json_folder'])
