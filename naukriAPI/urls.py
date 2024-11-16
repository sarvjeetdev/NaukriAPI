# urls.py
from django.urls import path
from .views import NaukriJobsListCreateView

urlpatterns = [
    path('jobs/', NaukriJobsListCreateView.as_view(), name='naukri-jobs-list-create'),
]
