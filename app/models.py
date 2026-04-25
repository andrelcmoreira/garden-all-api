import hashlib

from django.db import models


class DeviceConfiguration(models.Model):
    name = models.TextField()
    check_cfg_interval = models.IntegerField()
    activate_pump_interval = models.IntegerField()
    read_sensors_interval = models.IntegerField()
    cfg_hash = models.CharField(max_length=64, unique=True, editable=False)

    class Meta:
        db_table = 'device_cfg'

    def save(self, *args, **kwargs):
        cfg_id = f"{self.name}{self.check_cfg_interval} \
            {self.activate_pump_interval}{self.read_sensors_interval}" \
            .encode("utf-8")

        self.cfg_hash = hashlib.sha256(cfg_id).hexdigest()
        super().save(*args, **kwargs)


class Device(models.Model):
    name = models.TextField()
    model = models.TextField()
    mac_address = models.CharField(max_length=17, unique=True)
    fingerprint = models.CharField(max_length=64, unique=True, editable=False)
    cfg = models.ForeignKey(
        DeviceConfiguration,
        on_delete=models.SET_NULL,
        null=True,
        related_name='devices'
    )

    class Meta:
        db_table = 'device'

    def save(self, *args, **kwargs):
        dev_id = f"{self.model}{self.mac_address}".encode("utf-8")

        self.fingerprint = hashlib.sha256(dev_id).hexdigest()
        super().save(*args, **kwargs)


class DeviceEvent(models.Model):
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name='events'
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=50)
    event_data = models.JSONField()

    class Meta:
        db_table = 'device_event'
