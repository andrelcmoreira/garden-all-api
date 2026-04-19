from django.urls import path

from .views import (
    DeviceListCreateView,
    DeviceConfigDetailView,
    DeviceConfigListCreateView
)


urlpatterns = [
    path(
        'devices/',
        DeviceListCreateView.as_view(),
        name='device-list-create'
    ),
    path(
        'devices/<str:fingerprint>/config/',
        DeviceConfigDetailView.as_view(),
        name='device-config-detail'
    ),
    path(
        'configs/',
        DeviceConfigListCreateView.as_view(),
        name='config-list-create'
    )
]
