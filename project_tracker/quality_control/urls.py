from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugListView.as_view(), name='bugs_list'),
    path('features/', views.FeatureListView.as_view(), name='feature_list'),
    path('bugs/<int:bug_id>/', views.BugsDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('bugs/new/', views.create_bug_report, name='create_bug_report'),
    path('features/new/', views.create_feature_request, name='create_feature_request'),
]
