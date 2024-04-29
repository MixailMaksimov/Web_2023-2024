from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    another_page_url = reverse('tasks:another_page')
    quality_control_page_url = reverse('quality_control:index')
    html = f"<h1>Страница приложения tasks</h1>" \
           f"<h3><a href='{another_page_url}'>Перейти на другую страницу</a></h3>" \
           f"<h3><a href='{quality_control_page_url}'>Перейти к системе контроля качества</a></h3>"
    return HttpResponse(html)


def another_page(request):
    return HttpResponse("Это другая страница tasks")
