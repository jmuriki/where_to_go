from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from places.models import Place


def compose_place_details(place):
    images_urls = [
        img.image.url for img in place.images.all()
    ]
    details = {
        "title": place.title,
        "imgs": images_urls,
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat,
        }
    }
    return details


def get_place_json(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related('images'),
        pk=place_id,
    )
    details = compose_place_details(place)
    return JsonResponse(
        details,
        safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent': 2},
    )


def index(request):
    places_geojson = {
        "geo_json": {
            "type": "FeatureCollection",
            "features": [],
        }
    }
    places = Place.objects.all()
    for place in places:
        place_features = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    place.lng,
                    place.lat,
                ]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse("place_json", args=[place.id]),
            }
        }
        places_geojson["geo_json"]["features"].append(place_features)
    return render(request, "index.html", context=places_geojson)
