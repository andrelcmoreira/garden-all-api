from rest_framework import serializers

from .models import Device, DeviceConfiguration


class DeviceConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceConfiguration
        fields = [
            'id',
            'device_id',
            'check_cfg_interval',
            'activate_pump_interval',
            'read_sensors_interval'
        ]


class DeviceSerializer(serializers.ModelSerializer):
    cfg_id = DeviceConfigurationSerializer(read_only=True)

    class Meta:
        model = Device
        fields = [
            'id',
            'name',
            'model',
            'mac_address',
            'fingerprint',
            'cfg_id'
        ]
