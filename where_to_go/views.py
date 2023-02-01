from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from places.models import Place, Image


def show_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    template = loader.get_template('place.html')
    context = {"place": place}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def index(request):
    template = loader.get_template('index.html')
    context = {
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
        context["geo_json"]["features"].append(place_features)
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
