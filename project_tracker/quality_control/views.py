from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest


def index(request):
    bug_list_url = reverse('bug_list')
    feature_list_url = reverse('feature_list')
    html = f"<h1>Система контроля качества</h1>" \
           f"<h3><a href='{bug_list_url}'>Список всех багов</a></h3>" \
           f"<h3><a href='{feature_list_url}'>Запросы на улучшение</a><h3>"
    return HttpResponse(html)


def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
    for bug in bugs:
        bugs_html += f"<li><a href='{bug.id}/'>{bug.title}</a></li>"
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f"<li><a href='{feature.id}/'>{feature.title}</a></li>"
    features_html += '</ul>'
    return HttpResponse(features_html)


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>'
    return HttpResponse(response_html)


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p>'
    return HttpResponse(response_html)


from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('bug_list')
        feature_list_url = reverse('feature_list')
        html = f"<h1>Система контроля качества</h1>" \
               f"<h3><a href='{bug_list_url}'>Список всех багов</a></h3>" \
               f"<h3><a href='{feature_list_url}'>Запросы на улучшение</a><h3>"
        return HttpResponse(html)


from django.views.generic import ListView


class FeatureListView(ListView):
    model = FeatureRequest

    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        feature_html = '<h1>Список запросов на улучшения</h1>'
        for feature in features:
            feature_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
            feature_html += f'<ul><li>{feature.status}</li></ul>'
        feature_html += '</ul>'
        return HttpResponse(feature_html)


class BugListView(ListView):
    model = BugReport

    def get(self, request, *args, **kwargs):
        bugs = self.get_queryset()
        bugs_html = '<h1>Список отчетов об ошибках</h1>'
        for bug in bugs:
            bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
            bugs_html += f'<ul><li>{bug.status}</li></ul>'
        bugs_html += '</ul>'
        return HttpResponse(bugs_html)


from django.views.generic import DetailView


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>{feature.title}</h1>'
        response_html += f'<ul><li>{feature.description}</li>' \
                         f'<li>{feature.status}</li>' \
                         f'<li>{feature.priority}</li>' \
                         f'<li>{feature.project.name}</li>' \
                         f'<li>{feature.task.name}</li></ul>'
        return HttpResponse(response_html)


class BugsDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f'<h1>{bug.title}</h1>'
        response_html += f'<ul><li>{bug.description}</li>' \
                         f'<li>{bug.status}</li>' \
                         f'<li>{bug.priority}</li>' \
                         f'<li>{bug.project.name}</li>' \
                         f'<li>{bug.task.name}</li></ul>'
        return HttpResponse(response_html)
