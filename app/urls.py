"""
URL mapping for the application views.
"""
from django.urls import path

from .views import (
    DeviceListCreateView,
    DeviceDetailView,
    DeviceConfigurationDetailView,
    DeviceConfigurationListCreateView
)


urlpatterns = [
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path(
        'devices/<str:fingerprint>/',
        DeviceDetailView.as_view(),
        name='device-detail'
    ),
    path(
        'configs/',
        DeviceConfigurationListCreateView.as_view(),
        name='config-list-create'
    ),
    path(
        'configs/<int:pk>/',
        DeviceConfigurationDetailView.as_view(),
        name='config-detail'
    )
]
