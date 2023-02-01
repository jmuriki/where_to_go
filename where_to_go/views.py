from django.shortcuts import render, get_object_or_404

from places.models import Place, Image


def show_place(request, place_id):
    place = {"place": get_object_or_404(Place, pk=place_id)}
    return render(request, "place.html", context=place)


def index(request):
    places_geojson = {
        "geo_json": {
            "type": "FeatureCollection",
            "features": [],
        }
    }
    places = Place.objects.prefetch_related('images').all()
    for place in places:
        place_features = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    place.coordinates_lng,
                    place.coordinates_lat,
                ]
            },
            "properties": {
                "title": place.title,
                "placeId": place.placeId,
                "detailsUrl": place.detailsUrl,
            }
        }
        places_geojson["geo_json"]["features"].append(place_features)
    return render(request, "index.html", context=places_geojson)
