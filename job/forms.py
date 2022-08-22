from django import forms
from .models import Applicants

class ApplicantForm(forms.ModelForm):
     class Meta:
        model=Applicants
        fields=['name','email','website','cv','coverletter']
        