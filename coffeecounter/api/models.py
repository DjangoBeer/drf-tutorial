from django.db import models
from django.contrib.auth.models import User


class Badge(models.Model):
	title = models.CharField(max_length=100, blank=False, null=False)
	description = models.CharField(max_length=100, blank=False, null=False)
