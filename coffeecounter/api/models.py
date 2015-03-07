from django.db import models
from django.contrib.auth.models import User


class CoffeeUser(models.Model):
    user = models.OneToOneField(User)
    twitter = models.CharField(max_length=30, default='')


class Badge(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100)


class Consumption(models.Model):
    user = models.ForeignKey(User, related_name='consumptions')
    created = models.DateTimeField(auto_now_add=True)


class PoweredBadge(models.Model):
    user = models.ForeignKey(User)
    badge = models.ForeignKey(Badge)
    power = models.PositiveIntegerField(default=1)
