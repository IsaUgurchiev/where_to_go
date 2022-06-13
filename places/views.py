from django.shortcuts import render
from places.models import Place, PlaceImage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


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
                "placeId": place.id,
                "detailsUrl": reverse('place-detail', kwargs={'id': place.id})
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
    for img in place.image.all():
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