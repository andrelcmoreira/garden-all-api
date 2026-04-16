"""
URL mapping for the application views.
"""
from django.urls import path

from .views import (
    DeviceListCreateView,
    DeviceDetailView,
    DeviceConfigurationListCreateView
)


urlpatterns = [
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path(
        'devices/<int:pk>/',
        DeviceDetailView.as_view(),
        name='device-detail'
    ),
    path(
        'devices/<int:pk>/config/',
        DeviceConfigurationListCreateView.as_view(),
        name='device-config-list-create'
    )
]
