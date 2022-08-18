from django.db import models
from staff.models import Person


class TypeDoc(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Platform(models.Model):
    name = models.CharField(max_length=64, unique=True)
    link = models.CharField(max_length=256, null=True, blank=True)


class Certificate(models.Model):
    class Meta:
        verbose_name_plural = 'Сертифікати'

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=128)

    link = models.CharField(max_length=256)

    type_doc = models.ForeignKey(TypeDoc, models.CASCADE)

    platform = models.ForeignKey(
        Platform,
        models.CASCADE,
        null=True,
        blank=True,
    )

    number_of_hours = models.FloatField(
        null=True,
        blank=True,
    )

    date = models.DateField()

