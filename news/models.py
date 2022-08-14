from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    class Meta:
        verbose_name_plural = 'Новини'

    title = models.CharField(max_length=64, verbose_name='Заголовок')
    # author
    # categories
    # images
    body = RichTextField(blank=True, null=True)
    date_created = models.DateField(verbose_name='Дата публікації')
    is_published = models.BooleanField(default=True, verbose_name='Публікувати')
