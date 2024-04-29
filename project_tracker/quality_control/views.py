from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    bug_list_url = reverse('bug_list')
    feature_list_url = reverse('feature_list')
    html = f"<h1>Система контроля качества</h1>" \
           f"<h3><a href='{bug_list_url}'>Список всех багов</a></h3>" \
           f"<h3><a href='{feature_list_url}'>Запросы на улучшение</a><h3>"
    return HttpResponse(html)


def bug_list(request):
    return HttpResponse("<h1>Cписок отчетов об ошибках</h1>")


def feature_list(request):
    return HttpResponse("<h1>Список запросов на улучшение</h1>")


def bug_detail(request, bug_id):
    return HttpResponse(f"<h1>Список запросов на улучшение</h1>"
                        f"Детали бага {bug_id}")


def feature_detail(request, feature_id):
    return HttpResponse(f"<h1>Список запросов на улучшение</h1>"
                        f"Детали улучшения {feature_id}")

