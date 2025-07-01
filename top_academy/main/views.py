from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная страница',
        'content': 'Lorem ipsum dolor sit...',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О магазине',
        'content': 'Информация о магазине: Lorem ipsum dolor sit...',
    }
    return render(request, 'main/about.html', context)
