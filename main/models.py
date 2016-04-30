from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# There is also a User model, which is not explicitly written here because it is done automatically by django

# User:
# 	_id
# 	firstname
# 	lastname
# 	username
# 	password
# 	email

class Settings(models.Model):
	user = models.ForeignKey(User)
	timezone = models.CharField(max_length=50)
	contact_time = models.CharField(max_length=20)

class Goal(models.Model):
	user = models.ForeignKey(User)
	category = models.CharField(max_length=20)
	week_number = models.IntegerField()
	title = models.CharField(max_length=20)
	completed_bool = models.BooleanField(default=False)
	completed_date = models.DateField(auto_now=False, auto_now_add=False)
