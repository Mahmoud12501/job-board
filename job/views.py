from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Job
from .forms import ApplicantForm,AddJob
from .filters import JobFilter
from django.contrib.auth.decorators import login_required
# Create your views here.

def job_list(request):
    job_list=Job.objects.all()
    filter=JobFilter(request.GET,queryset=job_list)
    job_list=filter.qs
    pagintor=Paginator(job_list,5)
    page_num=request.GET.get('page')
    page_obj=pagintor.get_page(page_num)

    contxt={"jobs":page_obj,'myfilter':filter}

    return render(request,"job/all_job.html",contxt)

def job_detail(request,slug):
    job_detail=Job.objects.get(slug=slug)
   
    # applay job
    if request.method=='POST':
        form=ApplicantForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
        
            myform.job=job_detail
            myform.save()
    else:
        form=ApplicantForm()
        
    # if request.method=='POST':
    #     cv= ApplicantForm(request.POST,request.FILES)
    #     username=request.POST.get('name') 
    #     email=request.POST.get('email')
    #     website=request.POST.get('website')
    #     cv=(request.POST.get('cv'))   
    #     cover=request.POST.get('cover')
        
    #     data=Applicants(job=job_detail,name=username,email=email,website=website,cv=cv,coverletter=cover)
    #     data.save()

    contxt={"job":job_detail,"form":form}

    return render(request,"job/job_detail.html",contxt)

@login_required
def add_job(request):
    if request.method=='POST':
       form=AddJob(request.POST,request.FILES)
       if form.is_valid():
           myform=form.save(commit=False)
           myform.owner=request.user
           myform.save()
           return redirect(reverse('jobs:job_list'))      
    else:
        form=AddJob()
    return render(request,"job/add_job.html",{'form':form})