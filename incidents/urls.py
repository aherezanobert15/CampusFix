from django.urls import path
from . import views


urlpatterns = [
    path(
        'report/',
        views.report_incident,
        name='report_incident'
    ),
       path(
        'dashboard/',
        views.incident_dashboard,
        name='incident_dashboard'
    ),
]
