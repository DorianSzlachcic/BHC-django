from django.db import models

# Create your models here.

class Channel(models.Model):
    name = models.CharField(max_length=64)
    opened = models.BooleanField(default=False)
