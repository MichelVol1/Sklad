from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Iteam(models.Model):
    title = models.CharField(max_length=100, null=True)

    weight = models.PositiveIntegerField( null=True, blank=True)

    height = models.PositiveIntegerField( null=True, blank=True)

    length = models.PositiveIntegerField( null=True, blank=True)

    note = models.CharField(max_length=100, null=True,blank=True)

    data_posted = models.DateTimeField(auto_now_add=True, null=True)

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
