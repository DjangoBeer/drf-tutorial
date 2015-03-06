from django.db import models
from django.contrib.auth.models import User


class Badge(models.Model):
	title = models.CharField(max_length=100, blank=False, null=False)
	description = models.CharField(max_length=100, blank=False, null=False)


class Consumption(models.Model):
    user = models.ForeignKey(User, related_name='consumptions')
    created = models.DateTimeField(auto_now_add=True)


class PoweredBadge(models.Model):
    user = models.ForeignKey(User)
    badge = models.ForeignKey(Badge)
    power = models.PositiveIntegerField(default=1)
