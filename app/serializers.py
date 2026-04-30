from django.core.validators import RegexValidator
from rest_framework import serializers

from .models import (
    Device,
    DeviceConfiguration,
    DeviceEvent
)


class DeviceConfigurationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(
        allow_blank=False,
        required=True,
        error_messages={
            'blank': "The 'name' field cannot be blank",
            'required': "The 'name' field is required"
        }
    )
    check_cfg_interval = serializers.IntegerField(
        min_value=1,
        required=True,
        error_messages={
            'min_value': "The provided value for 'check_cfg_interval' must be greater than 0",
            'required': "The 'check_cfg_interval' field is required"
        }

    )
    activate_pump_interval = serializers.IntegerField(
        min_value=1,
        required=True,
        error_messages={
            'min_value': "The provided value for 'activate_pump_interval' must be greater than 0",
            'required': "The 'activate_pump_interval' field is required"
        }
    )
    read_sensors_interval = serializers.IntegerField(
        min_value=1,
        required=True,
        error_messages={
            'min_value': "The provided value for 'read_sensors_interval' must be greater than 0",
            'required': "The 'read_sensors_interval' field is required"
        }
    )

    class Meta:
        model = DeviceConfiguration
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(
        allow_blank=False,
        required=True,
        error_messages={
            'blank': "The 'name' field cannot be blank",
            'required': "The 'name' field is required"
        }
    )
    model = serializers.CharField(
        allow_blank=False,
        required=True,
        error_messages={
            'blank': "The 'model' field cannot be blank",
            'required': "The 'model' field is required"
        }
    )
    mac_address = serializers.CharField(
        allow_blank=False,
        required=True,
        validators=[
            RegexValidator(
                regex=r'^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$',
                message="The provided value for 'mac_address' is not a valid MAC address"
            )
        ],
        max_length=17,
        error_messages={
            'blank': "The 'mac_address' field cannot be blank",
            'required': "The 'mac_address' field is required"
        }
    )
    cfg = serializers.PrimaryKeyRelatedField(
        queryset=DeviceConfiguration.objects.all(),
        required=True,
        error_messages={
            'does_not_exist': "The provided 'cfg' does not exist",
            'required': "The 'cfg' field is required"
        }
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


class DeviceEventSerializer(serializers.ModelSerializer):
    device = serializers.PrimaryKeyRelatedField(
        queryset=Device.objects.all(),
        required=True,
        error_messages={
            'does_not_exist': "The provided 'device' does not exist",
            'required': "The 'device' field is required"
        }
    )
    event_type = serializers.CharField(
        allow_blank=False,
        required=True,
        error_messages={
            'blank': "The 'event_type' field cannot be blank",
            'required': "The 'event_type' field is required"
        }
    )
    event_data = serializers.JSONField()

    class Meta:
        model = DeviceEvent
        fields = '__all__'
