from django import forms
from .models import Applicants,Job
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class ApplicantForm(forms.ModelForm):
     class Meta:
        model=Applicants
        fields=['name','email','website','cv','coverletter']
        
class AddJob(forms.ModelForm):
   jop_describtion = forms.CharField(widget=SummernoteWidget)
   class Meta:
      model=Job
      fields='__all__'
      exclude=('slug','owner')
      