from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        'title': 'Honey - Головна',
        'content': "Магазин продуктів Honey",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Honey - Про нас',
        'content': "Про нас",
        'text_on_page': "Наш магазин крутий"
    }

    return render(request, 'main/about.html', context)