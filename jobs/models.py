from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=128)
    employer = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    typeOfWork = models.CharField(max_length=128, help_text="full-time, part-time, internship or other")
    contract = models.CharField(max_length=128, help_text="work contract, civil contract or B2B")
    operatingMode = models.CharField(max_length=128, help_text="remote, stationary or hybrid")
    jobDescription = models.TextField()
    requiredSkills = models.TextField()
    dateAdded = models.DateField()
    dateExpired = models.DateField()
    salary = models.IntegerField()