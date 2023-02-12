import os
import json
import shutil
import requests
from pathlib import Path
from urllib.parse import urlparse
from urllib.parse import unquote

from django.core.management.base import BaseCommand
from places.models import Place, Image


BASE_DIR = Path(__file__).absolute().parent.parent.parent.parent
MEDIA_ROOT = Path(f'{BASE_DIR}/media')


def get_paths(folder):
    paths = []
    for root, _, filenames in os.walk(Path(folder)):
        for name in filenames:
            path = os.path.join(root, name)
            paths.append(path)
    return paths


def check_for_system_files(path):
    system_files_extentions = ['.DS_Store']
    return any(extention in path for extention in system_files_extentions)


def get_filename_from_url(url):
    url_part = urlparse(url).path
    unquoted_url_part = unquote(url_part)
    filename = os.path.split(unquoted_url_part)[-1]
    return filename


def check_for_existence(img_name, imgs_paths):
    for img_path in imgs_paths:
        if img_name in os.path.split(img_path)[-1]:
            return True
    return False


def save_content(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(Path(path), 'wb') as file:
        file.write(response.content)


def fetch_images(place_json, imgs_paths):
    imgs_names = []
    for img_url in place_json['imgs']:
        img_name = get_filename_from_url(img_url)
        if not imgs_paths or not check_for_existence(img_name, imgs_paths):
            img_path = f'{MEDIA_ROOT}/{img_name}'
            save_content(img_url, img_path)
        imgs_names.append(img_name)
    return imgs_names


def load_places(json_folder):
    json_files_paths = get_paths(json_folder)
    imgs_paths = get_paths(MEDIA_ROOT)
    places_jsons = []
    for path in json_files_paths:
        if not check_for_system_files(path):
            with open(Path(path), 'r') as json_file:
                places_jsons.append(json.load(json_file))
    for place_json in places_jsons:
        place_json['imgs_names'] = fetch_images(
            place_json,
            imgs_paths,
        )
        place, _ = Place.objects.get_or_create(
            title=place_json['title'],
            description_short=place_json['description_short'],
            description_long=place_json['description_long'],
            coordinates_lng=place_json['coordinates']['lng'],
            coordinates_lat=place_json['coordinates']['lat'],
        )
        for img_name in place_json['imgs_names']:
            Image.objects.get_or_create(place=place, image=img_name)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '-j',
            '--json_folder',
            default=False,
        )
        parser.add_argument(
            '-i',
            '--images_folder',
            default=False,
        )

    def handle(self, *args, **options):
        Path(MEDIA_ROOT).mkdir(parents=True, exist_ok=True)
        if options['images_folder']:
            images_paths = get_paths(options['images_folder'])
            for image in images_paths:
                shutil.copy(image, MEDIA_ROOT)
        if options['json_folder']:
            load_places(options['json_folder'])
        else:
            print('Add path to json files folder & images folder or use -h')
