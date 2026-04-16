from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=17, unique=True)
    fingerprint = models.CharField(max_length=32)
    cfg_id = models.OneToOneField(
        'DeviceConfiguration',
        on_delete=models.CASCADE,
        related_name='device',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'device'


class DeviceConfiguration(models.Model):
    device_id = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name='configurations'
    )
    check_cfg_interval = models.IntegerField()
    activate_pump_interval = models.IntegerField()
    read_sensors_interval = models.IntegerField()

    class Meta:
        db_table = 'device_cfg'
