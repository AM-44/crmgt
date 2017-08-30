from django.db import models
from django.contrib.auth.models import User

from shortuuidfield import ShortUUIDField


class Currency(models.Model):
    uuid = ShortUUIDField(unique=True)
    currency_name = models.CharField(max_length=80)
    desc = models.TextField(blank=True)
    address_one = models.CharField(max_length=200)
    address_two = models.CharField(max_length=200, blank=True)
    exchange = models.CharField(max_length=50)
    investment = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    owner = models.ForeignKey(User)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'currencies'

    def __unicode__(self):
        return u"%s" % self.currency_name

    @models.permalink
    def get_absolute_url(self):
        return 'currency_detail', [self.uuid]

    @models.permalink
    def get_update_url(self):
        return 'currency_update', [self.uuid]

    @models.permalink
    def get_delete_url(self):
        return 'account_delete', [self.uuid]