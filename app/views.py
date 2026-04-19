from django.http import Http404
from rest_framework import generics

#from .exceptions import ConfigurationNotFound
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

    #def get_object(self):
    #    cfg_id = self.kwargs.get('pk')

    #    try:
    #        return generics.get_object_or_404(self.get_queryset(), pk=cfg_id)
    #    except Http404 as exc:
    #        raise ConfigurationNotFound(cfg_id) from exc


class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'fingerprint'
