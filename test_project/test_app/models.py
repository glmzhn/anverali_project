from django.contrib.auth.models import User
from django.db import models


class Orderer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)


class Executor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    job_title = models.CharField(max_length=100, null=False, blank=False)
    job_experience = models.BooleanField(null=True, blank=True, default=None)


class Experience(models.Model):
    user = models.OneToOneField(Executor, on_delete=models.CASCADE)
    years = models.IntegerField(null=True, blank=True)
    months = models.IntegerField(null=True, blank=True)
    weeks = models.IntegerField(null=True, blank=True)
