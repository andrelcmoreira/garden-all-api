from rest_framework import serializers

from .exceptions import InvalidField
from .models import Device, DeviceConfiguration


class DeviceConfigurationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(allow_blank=True)
    check_cfg_interval = serializers.IntegerField()
    activate_pump_interval = serializers.IntegerField()
    read_sensors_interval = serializers.IntegerField()

    class Meta:
        model = DeviceConfiguration
        fields = '__all__'

    def validate_name(self, value) -> str:
        if not value.strip():
            raise InvalidField('name')

        return value

    def validate_check_cfg_interval(self, value) -> int:
        if value <= 0:
            raise InvalidField('check_cfg_interval')

        return value

    def validate_activate_pump_interval(self, value) -> int:
        if value <= 0:
            raise InvalidField('activate_pump_interval')

        return value

    def validate_read_sensors_interval(self, value) -> int:
        if value <= 0:
            raise InvalidField('read_sensors_interval')

        return value


class DeviceSerializer(serializers.ModelSerializer):
    cfg = serializers.PrimaryKeyRelatedField(
        queryset=DeviceConfiguration.objects.all()
    )

    class Meta:
        model = Device
        fields = [
            'id',
            'name',
            'model',
            'mac_address',
            'cfg'
        ]
