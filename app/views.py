from rest_framework import generics

from .models import Device, DeviceConfiguration
from .serializers import (
    DeviceEventSerializer,
    DeviceSerializer,
    DeviceConfigurationSerializer
)


class DeviceListCreateView(generics.ListCreateAPIView):
    """View for listing and creating devices."""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceConfigListCreateView(generics.ListCreateAPIView):
    """View for listing and creating device configurations."""
    queryset = DeviceConfiguration.objects.all()
    serializer_class = DeviceConfigurationSerializer


class DeviceConfigDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting a device configuration."""
    serializer_class = DeviceConfigurationSerializer

    def get_object(self):
        """
        Override get_object to retrieve the device configuration based on
        the device fingerprint.
        """
        fingerprint = self.kwargs.get("fingerprint")

        device = generics.get_object_or_404(
            Device.objects.select_related("cfg"),
            fingerprint=fingerprint
        )

        if not device.cfg:
            raise generics.Http404("Configuration not found for this device")

        return device.cfg


class DeviceEventListCreateView(generics.ListCreateAPIView):
    """View for listing and creating device events."""
    serializer_class = DeviceEventSerializer

#    def get_queryset(self):
#        fingerprint = self.kwargs.get("fingerprint")
#
#        device = generics.get_object_or_404(
#            Device.objects.select_related("cfg"),
#            fingerprint=fingerprint
#        )
#
#        if not device.cfg:
#            raise generics.Http404("Configuration not found for this device")
#
#        return device.cfg.events.all()
