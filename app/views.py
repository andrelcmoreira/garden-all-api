from rest_framework import generics

from .models import Device, DeviceConfiguration
from .serializers import DeviceSerializer, DeviceConfigurationSerializer


class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceConfigListCreateView(generics.ListCreateAPIView):
    queryset = DeviceConfiguration.objects.all()
    serializer_class = DeviceConfigurationSerializer


class DeviceConfigDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceConfigurationSerializer

    def get_object(self):
        fingerprint = self.kwargs.get("fingerprint")

        device = generics.get_object_or_404(
            Device.objects.select_related("cfg"),
            fingerprint=fingerprint
        )

        if not device.cfg:
            raise generics.Http404("Configuration not found for this device")

        return device.cfg
