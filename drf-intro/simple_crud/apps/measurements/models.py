from django.db import models


class TimestampFields(models.Model):
    """Абстрактный класс c данными о времени создания и обновления"""
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        """Объявляем этот класс абстрактным, его невозможно инстанцировать и он не имеет своей таблицы, все наследники
        от него становятся реальными классами, пока у них также не будет объявлено abstract = True"""
        abstract = True


class Project(TimestampFields):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Measurement(TimestampFields):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='measurements')
    photo = models.ImageField(null=True, blank=True)
