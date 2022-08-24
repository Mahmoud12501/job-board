from django import forms
from .models import Applicants,Job

class ApplicantForm(forms.ModelForm):
     class Meta:
        model=Applicants
        fields=['name','email','website','cv','coverletter']
        
class AddJob(forms.ModelForm):
   class Meta:
      model=Job
      fields='__all__'
      exclude=('slug','owner')
   