from __future__ import unicode_literals

from django.db import models
from Login.models import User

# Create your models here.
class Project(models.Model):
	projectid = models.IntegerField(primary_key=True,unique=True)
	name = models.CharField(max_length=75, null=True, blank=True)
	desc = models.CharField(max_length=100, null=True, blank=True)
	adminid = models.ForeignKey(User, on_delete=models.CASCADE)

class Member(models.Model):
	memberid = models.IntegerField(primary_key=True,unique=True)
	userid = models.ForeignKey(User, on_delete=models.CASCADE)
	projectid = models.ForeignKey(Project, on_delete=models.CASCADE)
	isadmin = models.BooleanField(null=False)

class Task(models.Model):
	taskid = models.IntegerField(primary_key=True,unique=True)
	desc = models.CharField(max_length=100, null=True, blank=True)
	status = models.CharField(max_length=20, null=True, blank=True)
	assignedto = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='To')
	assignedby = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='By')