from django.core.management.base import BaseCommand
from products.models import Product
import glob
import json
import os
import pdb

class Command(BaseCommand):
    args = 'dir (optional) : The directory in which the JSON files can be found.'
    help = 'This command populates the database with products given the data from JSON files in a directory.'

    def _add_products_from_dir(self):
        TEMP_JSON = os.path.join(os.path.expanduser('~'), 'TEMP_JSON_FILES')
        for file in glob.glob(os.path.join(TEMP_JSON, "*.json")):
            with open(file) as json_data:
                # assume the dictionary has identical parameter names as model
                d = json.load(json_data)
                # pdb.set_trace()
                prod, created = Product.objects.update_or_create(
                        name=d['name'], brand=d['brand'], defaults=d)

    def handle(self, *args, **options):
        self._add_products_from_dir()
