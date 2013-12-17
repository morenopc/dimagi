from django.db import models

from model_utils.models import TimeStampedModel


class MathEngineHistory(TimeStampedModel):
    """Math engime history model"""
    ip = models.GenericIPAddressField()
    values = models.CharField(max_length=255)
    sum = models.IntegerField()
    product = models.IntegerField()

    def __unicode__(self):
        return 'ip: %s, timestamp: %s, values: %s, sum: %s, product: %s' % (
            self.ip, self.created, self.values, self.sum, self.product)
