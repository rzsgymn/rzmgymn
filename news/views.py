from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News

COUNT_NEWS_OF_PAGE = 9


def get_list_of_pages(active_n: int, end_n: int) -> tuple:
    """
    :param active_n: active number of page
    :param end_n: end number of page
    :return: first class name, last class name, list for render html
    get_list_of_pages(1, 3) == 'disabled', '', [1, 2, 3]
    get_list_of_pages(55, 100) == '', '', [1, 2, 0, 53, 54, 55, 56, 57, 0, 99, 100]
    """

    # lst = ['disabled' if active_n == 1 else '']
    lst = []
    if active_n <= 5:
        [lst.append(n) for n in range(1, active_n)]
    else:
        lst.extend([1, 2, 0, active_n - 2, active_n - 1])

    if active_n + 5 >= end_n:
        [lst.append(n) for n in range(active_n, end_n + 1)]
    else:
        lst.extend([active_n, active_n + 1, active_n + 2, 0, end_n - 1, end_n])
    # lst.append('disabled' if active_n == end_n else '')
    return (
        'disabled' if active_n == 1 else '',
        'disabled' if active_n == end_n else '',
        lst
    )


def blog(request):
    news = News.objects.filter(is_published=True).order_by('-date_created')
    paginator = Paginator(news, COUNT_NEWS_OF_PAGE)
    page_number = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(page_number)

    end_n = paginator.page_range.stop - 1
    if page_number > end_n:
        page_number = end_n

    class_first_page, class_last_page, list_of_pages = get_list_of_pages(page_number, end_n)
    context = {
        'news': page_obj.object_list,
        'list_of_pages': list_of_pages,
        'class_first_page': class_first_page,
        'class_last_page': class_last_page,
        'page_number': page_number,
        'next_link': page_number + 1,
        'previous': page_number - 1
    }
    return render(request, 'news/blog.html', context=context)
