from django.shortcuts import render

from .models import Facility, Testimonial
from administration.models import Administration


def index(request):
    facilities = Facility.objects.all()
    testimonials = Testimonial.objects.all()
    administration = []
    for admin in Administration.objects.all():
        social_network = []
        for item in admin.person_admin.socialnetworkofuser_set.all():
            social_network.append({
                "link": item.link,
                "class_name": item.type_of_social_network.class_name,
            })

        administration.append({
            "name": str(admin),
            "position": str(admin.position),
            "social_network": social_network,
            "src": admin.person_admin.photo.url if admin.person_admin.photo else None,
        })

    context = {
        "facilities": facilities,
        "testimonials": testimonials,
        "administration": administration,
    }
    return render(request, 'core/index.html', context=context)
