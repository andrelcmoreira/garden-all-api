import hashlib

from django.db import models


class Device(models.Model):
    name = models.TextField()
    model = models.TextField()
    mac_address = models.CharField(max_length=17, unique=True)
    fingerprint = models.CharField(max_length=32, unique=True, editable=False)
    cfg = models.ForeignKey('DeviceConfiguration', on_delete=models.CASCADE)

    class Meta:
        db_table = 'device'

    def save(self, *args, **kwargs):
        dev_id = f"{self.model}{self.mac_address}".encode("utf-8")

        self.fingerprint = hashlib.md5(dev_id).hexdigest()
        super().save(*args, **kwargs)


class DeviceConfiguration(models.Model):
    name = models.TextField()
    check_cfg_interval = models.IntegerField()
    activate_pump_interval = models.IntegerField()
    read_sensors_interval = models.IntegerField()

    class Meta:
        db_table = 'device_cfg'
