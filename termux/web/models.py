from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class call_log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    type = models.CharField(max_length=8)
    ## date = models.DateTimeField(max_length=50)
    date = models.CharField(max_length=50)
    duration = models.CharField(max_length=10)


class contact_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)


class clipboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)


class sms_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    type = models.CharField(max_length=8)
    ##received = models.DateTimeField(max_length=50)
    received = models.CharField(max_length=50)
    read = models.BooleanField()

class Token(models.Model):
    token = models.CharField(max_length=48)
    user = models.OneToOneField(User, on_delete=models.CASCADE)