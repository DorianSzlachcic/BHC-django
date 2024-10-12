from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=128)
    employer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=128)
    typeOfWork = models.CharField(max_length=128, help_text="full-time, part-time, internship or other")
    contract = models.CharField(max_length=128, help_text="work contract, civil contract or B2B")
    operatingMode = models.CharField(max_length=128, help_text="remote, stationary or hybrid")
    jobDescription = models.TextField()
    requiredSkills = models.TextField()
    dateAdded = models.DateField(auto_now_add=True)
    dateExpired = models.DateField()
    salary = models.IntegerField()