from django.urls import path
from interview import views

urlpatterns = [
    path('issues/', views.ListIssuesView.as_view(), name='issues'),
    path('', views.ListIssuesView.as_view(), name='issues_empty'),
    path('issues/add/', views.AddIssueView.as_view(), name='add_issue')
]
