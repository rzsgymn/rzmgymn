from django.db import models
from staff.models import Person


class Lesson(models.Model):
    class Meta:
        verbose_name_plural = 'Уроки'

    name = models.CharField(max_length=64, unique=True, verbose_name="назва")

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Категорії'

    name = models.CharField(max_length=64, unique=True, verbose_name="назва")

    def __str__(self):
        return self.name


class Rank(models.Model):
    class Meta:
        verbose_name_plural = 'Звання'

    name = models.CharField(max_length=64, unique=True, verbose_name="назва")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    class Meta:
        verbose_name_plural = 'Вчителі'

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name='Працівник',
    )

    lessons = models.ManyToManyField(Lesson, verbose_name="уроки")

    categories = models.ForeignKey(Category, models.CASCADE, verbose_name="категорія")

    ranks = models.ManyToManyField(
        Rank,
        blank=True,
        verbose_name="звання"
    )

    def __str__(self):
        return self.person.get_fullname()
