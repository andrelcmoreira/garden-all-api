from rest_framework import generics

from .models import Device, DeviceConfiguration
from .serializers import DeviceSerializer, DeviceConfigurationSerializer


class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceConfigurationListCreateView(generics.ListCreateAPIView):
    queryset = DeviceConfiguration.objects.all()
    serializer_class = DeviceConfigurationSerializer


class DeviceConfigurationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceConfiguration.objects.all()
    serializer_class = DeviceConfigurationSerializer


class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'fingerprint'
