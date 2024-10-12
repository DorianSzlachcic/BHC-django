from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from accounts.models import Company

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class RegisterCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['companyName','about','fieldOfWork']