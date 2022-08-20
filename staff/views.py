from django.shortcuts import render, get_object_or_404

from .models import Person
from teachers.models import Lesson, Category


def staff(request):
    persons = Person.objects.filter(liberated=True)
    context = {
        "persons": persons,
    }
    return render(request, 'staff/staff.html', context=context)


def staff_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)

    info_about_teacher = None
    if hasattr(person, 'teacher'):
        teacher_category = person.teacher.categories
        teacher_ranks = ', '.join(map(str, person.teacher.ranks.all()))
        info_about_teacher = f'{teacher_category}, {teacher_ranks}' if teacher_ranks else teacher_category

    context = {
        'person': person,
        'info_about_teacher': info_about_teacher,
        'certificates': person.certificate_set.order_by('-date'),
        'lessons': Lesson.objects.order_by('name'),
        'categories': Category.objects.order_by('-mass'),
    }
    return render(request, 'staff/single.html', context=context)
