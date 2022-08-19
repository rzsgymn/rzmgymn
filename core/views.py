from django.http import JsonResponse
from django.shortcuts import render

from news.models import News
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
    news = News.objects.filter(is_published=True).order_by('-date_created')[:3]
    context = {
        "facilities": facilities,
        "testimonials": testimonials,
        "administration": administration,
        "news": news,
    }
    return render(request, 'core/index.html', context=context)


def get_json_menu(request):
    json = {
        'data': [
            {
                'name': 'Головна',
                'link': '',
            },
            {
                'name': 'Про нас',
                'link': '/about',
            },
            {
                'name': 'Новини',
                'link': '/blog',
            },
            {
                'name': 'Teachers',
                'link': '/teachers',
            },
            {
                'name': 'Галерея',
                'link': '/galeru',
            },
            {
                'name': 'Pages',
                'sub_link': [
                    {
                        'name': 'Blog Grid',
                        'link': '',
                    },
                    {
                        'name': 'Blog Detail',
                        'link': '',
                    },
                ]
            },
            {
                'name': 'Контакти',
                'link': '/contact',
            },
        ]
    }

    return JsonResponse(json)
