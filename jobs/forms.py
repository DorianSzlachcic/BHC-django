from django.forms import ModelForm
from .models import Job

class JobForm(ModelForm):   
    class Meta:
        model = Job
        fields = ["title", "location", "typeOfWork", "contract", "operatingMode", "jobDescription", "requiredSkills", "dateExpired", "salary"]