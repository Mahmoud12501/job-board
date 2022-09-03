from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import  Info
# Create your views here.
def send_email(request):
    info=Info.objects.first()
    if request.method=='POST':
        
       
        subject=request.POST['subject']
        email=request.POST['email']
        message=request.POST['msg']
    
        
        send_mail(
            subject,
            f"{email}\n {message}",
            email,
            [settings.EMAIL_HOST_USER]  
            
        )
    
    return render(request,"contact/contact.html",{'info':info})