from django.contrib import admin

from .models import Facility, Testimonial, Menu, Alerts


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "type_menu",
    )


@admin.register(Alerts)
class AlertsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "style",
        "is_published",
    )


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "class_name_icon",
        "description",
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "show_photo",
        "text",
    )
