from django.contrib import admin

from .models import Person, SocialNetworkOfUser, TypeOfSocialNetwork, TypeOfAdministrativePosition, Administration


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


@admin.register(TypeOfAdministrativePosition)
class TypeOfAdministrativePositionAdmin(admin.ModelAdmin):
    list_display = (
        'type_position',
    )


@admin.register(Administration)
class AdministrationAdmin(admin.ModelAdmin):
    list_display = (
        'person_admin',
        'position',
    )

# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = (
#         'get_initials',
#         'show_photo',
#         'birthday',
#         'liberated',
#     )
