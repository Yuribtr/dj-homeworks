import csv
import datetime

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            # phone_reader = csv.reader(csvfile, delimiter=';')
            phone_reader = csv.DictReader(csvfile, delimiter=';')
            # пропускаем заголовок
            # next(phone_reader)

            for item in phone_reader:
                # item['id'] = int(item['id'])
                # item['price'] = int(item['price'])
                # item['release_date'] = datetime.datetime.now().date()
                # item['lte_exists'] = bool(item['lte_exists'])
                # p = Phone(item)
                p = Phone()
                p.id = int(item['id'])
                p.name = item['name']
                p.image = item['image']
                p.price = int(item['price'])
                p.release_date = datetime.datetime.now().date()
                p.lte_exists = bool(item['lte_exists'])
                p.slug = slugify(p.name)
                p.save()
