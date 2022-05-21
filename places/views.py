from django.shortcuts import render
from places.models import Place, PlaceImage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    places = Place.objects.all()

    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": "moscow_legends",
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
            }
        })

    data = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'index.html', {'places': data})


def place_detail(request, id):
    place = get_object_or_404(Place, pk=id)
    images = []
    for img in place.placeimage_set.all():
        images.append(img.image.url)
    data = {
        'title': place.title,
        'imgs': images,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        },
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})