from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job
from .forms import ApplicantForm
# Create your views here.

def job_list(request):
    job_list=Job.objects.all()
    pagintor=Paginator(job_list,5)
    page_num=request.GET.get('page')
    page_obj=pagintor.get_page(page_num)

    contxt={"jobs":page_obj}

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

    contxt={"job":job_detail,"form":form}

    return render(request,"job/job_detail.html",contxt)
