import logging
import requests

from io import BytesIO
from django.core.management import BaseCommand

from places.models import Place, PlaceImage

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Load information about places with media files'

    def add_arguments(self, parser):
        parser.add_argument('resource_url', type=str)

    def handle(self, *args, **options):
        resource_url = options['resource_url']

        logger.info(f'START LOADING DATA FROM RESOURCE {resource_url}')

        try:
            response = requests.get(resource_url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logger.error(f'UNABLE TO LOAD DATA FROM RESOURCE {resource_url}, details: {e}')
            return

        serialized_places = response.json()
        place, created = Place.objects.get_or_create(
            title=serialized_places['title'],
            defaults={
                'title': serialized_places['title'],
                'description_short': serialized_places['description_short'],
                'description_long': serialized_places['description_long'],
                'lng': serialized_places['coordinates']['lng'],
                'lat': serialized_places['coordinates']['lat']
            }
        )

        if not created:
            logger.info(f'UPDATED PLACE {place}')
            logger.info(f'END LOADING DATA FROM RESOURCE {resource_url}')
            return

        for position_index, img_url in enumerate(serialized_places['imgs'], start=1):
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                logger.error(f'UNABLE TO SAVE IMAGE FROM FROM RESOURCE {img_url}, details: {e}')
                continue

            img = BytesIO(img_response.content)
            place_image, img_created = PlaceImage.objects.get_or_create(
                place=place,
                position=position_index
            )
            place_image.image.save(f'place-{place.id}-img-{position_index}', img, save=True)

        logger.info(f'CREATED PLACE {place}')
        logger.info(f'END LOADING DATA FROM RESOURCE {resource_url}')
