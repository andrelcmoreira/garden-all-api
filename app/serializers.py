from django.core.validators import RegexValidator
from rest_framework import serializers

from .error import ERROR_MSGS
from .models import (
    Device,
    DeviceConfiguration,
    DeviceEvent
)


class DeviceConfigurationSerializer(serializers.ModelSerializer):
    """Serializer for DeviceConfiguration model."""
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(
        allow_blank=False,
        required=True,
        error_messages={
            'blank': ERROR_MSGS['blank'].format('name'),
            'required': ERROR_MSGS['required'].format('name')
        }
    )
    check_cfg_interval = serializers.IntegerField(
        min_value=1,
        required=True,
        error_messages={
            'min_value': ERROR_MSGS['min_value'].format('check_cfg_interval'),
            'required': ERROR_MSGS['required'].format('check_cfg_interval')
        }

    )
    activate_pump_interval = serializers.IntegerField(
        min_value=1,
        required=True,
        error_messages={
            'min_value': ERROR_MSGS['min_value'].format('activate_pump_interval'),
            'required': ERROR_MSGS['required'].format('activate_pump_interval')
        }
    )
    read_sensors_interval = serializers.IntegerField(
        min_value=1,
        required=True,
        error_messages={
            'min_value': ERROR_MSGS['min_value'].format('read_sensors_interval'),
            'required': ERROR_MSGS['required'].format('read_sensors_interval')
        }
    )

    class Meta:
        """Meta class for DeviceConfigurationSerializer."""
        model = DeviceConfiguration
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    """Serializer for Device model."""
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(
        allow_blank=False,
        required=True,
        error_messages={
            'blank': ERROR_MSGS['blank'].format('name'),
            'required': ERROR_MSGS['required'].format('name')
        }
    )
    model = serializers.CharField(
        allow_blank=False,
        required=True,
        error_messages={
            'blank': ERROR_MSGS['blank'].format('model'),
            'required': ERROR_MSGS['required'].format('model')
        }
    )
    mac_address = serializers.CharField(
        allow_blank=False,
        required=True,
        validators=[
            RegexValidator(
                regex=r'^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$',
                message=ERROR_MSGS['invalid'].format('mac_address')
            )
        ],
        max_length=17,
        error_messages={
            'blank': ERROR_MSGS['blank'].format('mac_address'),
            'required': ERROR_MSGS['required'].format('mac_address'),
        }
    )
    cfg = serializers.PrimaryKeyRelatedField(
        queryset=DeviceConfiguration.objects.all(),
        required=True,
        error_messages={
            'does_not_exist': ERROR_MSGS['does_not_exist'].format('cfg'),
            'required': ERROR_MSGS['required'].format('cfg')
        }
    )

    class Meta:
        """Meta class for DeviceSerializer."""
        model = Device
        fields = '__all__'


class DeviceEventSerializer(serializers.ModelSerializer):
    """Serializer for DeviceEvent model."""
    device = serializers.PrimaryKeyRelatedField(
        queryset=Device.objects.all(),
        required=True,
        error_messages={
            'does_not_exist': ERROR_MSGS['does_not_exist'].format('device'),
            'required': ERROR_MSGS['required'].format('device')
        }
    )
    event_type = serializers.CharField(
        allow_blank=False,
        required=True,
        error_messages={
            'blank': ERROR_MSGS['blank'].format('event_type'),
            'required': ERROR_MSGS['required'].format('event_type')
            }
    )
    event_data = serializers.JSONField()

    class Meta:
        """Meta class for DeviceEventSerializer."""
        model = DeviceEvent
        fields = '__all__'
