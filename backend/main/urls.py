from django.urls import path
from .views import *


urlpatterns = [
    path('projects/', FetchProjectsAPI.as_view(), name='fetch_projects'),
    path('custom_request/', CustomProjectRequestAPI.as_view(), name='custom_request'),
    path('select_project/', SelectProjectAPI.as_view(), name='select_project'),
]