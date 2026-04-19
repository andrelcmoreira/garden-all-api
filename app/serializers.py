#import re
#from django.core.validators import RegexValidator
from rest_framework import serializers

from .models import Device, DeviceConfiguration


class DeviceConfigurationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        allow_blank=False,
        error_messages={
            'blank': "The 'name' field cannot be blank",
            'required': "The 'name' field is required"
        }
    )
    check_cfg_interval = serializers.IntegerField(
        min_value=1,
        error_messages={
            'min_value': "The provided value for 'check_cfg_interval' must be greater than 0",
            'required': "The 'check_cfg_interval' field is required"
        }

    )
    activate_pump_interval = serializers.IntegerField(
        min_value=1,
        error_messages={
            'min_value': "The provided value for 'activate_pump_interval' must be greater than 0",
            'required': "The 'activate_pump_interval' field is required"
        }
    )
    read_sensors_interval = serializers.IntegerField(
        min_value=1,
        error_messages={
            'min_value': "The provided value for 'read_sensors_interval' must be greater than 0",
            'required': "The 'read_sensors_interval' field is required"
        }
    )

    class Meta:
        model = DeviceConfiguration
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        allow_blank=False,
        error_messages={
            'blank': "The 'name' field cannot be blank",
            'required': "The 'name' field is required"
        }
    )
    model = serializers.CharField(
        allow_blank=False,
        error_messages={
            'blank': "The 'model' field cannot be blank",
            'required': "The 'model' field is required"
        }
    )
    mac_address = serializers.CharField(
        allow_blank=False,
        #pattern=r'^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$',
        max_length=17
    )
    cfg = serializers.PrimaryKeyRelatedField(
        queryset=DeviceConfiguration.objects.all(),
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
