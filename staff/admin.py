from django.contrib import admin

from .models import Person, SocialNetworkOfUser, TypeOfSocialNetwork


@admin.register(TypeOfSocialNetwork)
class SocialNetworkOfUserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'class_name',
    )


@admin.register(SocialNetworkOfUser)
class SocialNetworkOfUserAdmin(admin.ModelAdmin):
    list_display = (
        'person',
        '__str__',
        'link',
    )


class SocialNetworkOfUserInline(admin.StackedInline):
    model = SocialNetworkOfUser


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        # 'get_initials',
        'show_photo',
        'birthday',
        'liberated',
    )

    inlines = [SocialNetworkOfUserInline]
