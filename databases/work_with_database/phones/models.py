from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    image = models.TextField()
    price = models.IntegerField()
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()
    slug = models.TextField(default=slugify(name))
