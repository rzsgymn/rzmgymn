import os

from django.db import models
from django.dispatch import receiver
from django.utils.html import mark_safe


class TypeOfSocialNetwork(models.Model):
    class Meta:
        verbose_name_plural = "Види соціальних мереж"

    name = models.CharField(max_length=32, verbose_name='назва')
    class_name = models.CharField(
        max_length=32,
        help_text='назви класів шукайте за посиланням https://fortawesome.com/sets/font-awesome-5-brands',
        verbose_name="ім'я класу"
    )

    def __str__(self):
        return self.name


class SocialNetworkOfUser(models.Model):
    class Meta:
        verbose_name_plural = "Соціальні мережі користувачів"

    type_of_social_network = models.ForeignKey(
        'TypeOfSocialNetwork',
        on_delete=models.CASCADE,
        verbose_name='Вид соціальної мережі'
    )
    link = models.CharField(max_length=255)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return self.type_of_social_network.name


class Person(models.Model):
    class Meta:
        verbose_name_plural = "Працівники"

    __SIZE_PHOTO = 80

    liberated = models.BooleanField(default=True, verbose_name='працює')

    sex = models.CharField(
        max_length=36,
        choices=(
            ('woman', 'жіноча'),
            ('man', 'чоловіча'),
        ),
        verbose_name='стать'
    )

    lastname = models.CharField(max_length=32, verbose_name="прізвище")
    firstname = models.CharField(max_length=32, verbose_name="ім'я")
    patronymic = models.CharField(max_length=32, verbose_name="по батькові")

    photo = models.ImageField(
        upload_to='staff',
        verbose_name='фото',
        help_text='фото має бути розміром 300x300 px',
        null=True,
        blank=True
    )

    birthday = models.DateField()
    phone = models.CharField(max_length=16, null=True, blank=True, verbose_name='телефон')
    other_phone = models.CharField(max_length=16, null=True, blank=True, verbose_name='додатковий телефон')

    def __str__(self):
        return self.get_fullname()

    def get_initials(self):
        return f'{self.lastname} {self.firstname[0]}. {self.patronymic[0]}.'

    def get_fullname(self):
        return f'{self.lastname} {self.firstname} {self.patronymic}'

    @property
    def show_photo(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width="{self.__SIZE_PHOTO}" height="{self.__SIZE_PHOTO}" />')
        return mark_safe(f'<img src="/static/img/user.png" width="{self.__SIZE_PHOTO}" height="{self.__SIZE_PHOTO}" />')


@receiver(models.signals.post_delete, sender=Person)
def auto_delete_file_on_delete(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(models.signals.pre_save, sender=Person)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    if not instance.pk:
        return False

    try:
        old_file = Person.objects.get(pk=instance.pk).photo
    except Person.DoesNotExist:
        return False

    new_file = instance.photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class TypeOfAdministrativePosition(models.Model):
    class Meta:
        verbose_name_plural = 'Види адміністративної посади'

    type_position = models.CharField(
        max_length=64,
        verbose_name='посада',
        help_text='приклад: Директор гімназії | Заступник директора з навчально-виховної роботи...'
    )

    def __str__(self):
        return self.type_position


class Administration(models.Model):
    class Meta:
        verbose_name_plural = 'Адміністрація'

    position = models.ForeignKey(
        TypeOfAdministrativePosition,
        on_delete=models.CASCADE,
        verbose_name='посада'
    )

    person_admin = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name='працівник',
    )

    def __str__(self):
        return self.person_admin.get_fullname()

