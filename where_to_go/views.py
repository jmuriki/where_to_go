from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    context = {
        "geo_json": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [37.62, 55.793676]
                    },
                    "properties": {
                        "title": "«Легенды Москвы",
                        "placeId": "moscow_legends",
                        "detailsUrl": "/static/places/moscow_legends.json"
                    }
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [37.64, 55.753676]
                    },
                    "properties": {
                        "title": "Крыши24.рф",
                        "placeId": "roofs24",
                        "detailsUrl": "/static/places/roofs24.json"
                    }
                }
            ]
        }
    }
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
