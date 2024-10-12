from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    companyName = models.CharField(max_length=128)
    ownerID = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)
    about = models.TextField()
    fieldOfWork = models.CharField(max_length=128)