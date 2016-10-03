from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	userid = models.IntegerField(primary_key=True,unique=True)
	name = models.CharField(max_length=75, null=True, blank=True)
	email = models.EmailField(unique=True, max_length=75, blank=True, null=True)
	password = models.CharField(max_length=75, blank=True, null=True)
	isadmin = models.BooleanField(null=False)