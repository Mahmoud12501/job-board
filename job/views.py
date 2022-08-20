from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job
# Create your views here.

def job_list(request):
    job_list=Job.objects.all()
    pagintor=Paginator(job_list,1)
    page_num=request.GET.get('page')
    page_obj=pagintor.get_page(page_num)

    contxt={"jobs":page_obj}

    return render(request,"job/all_job.html",contxt)

def job_detail(request,id):
    job_detail=Job.objects.get(pk=id)
    contxt={"job":job_detail}

    return render(request,"job/job_detail.html",contxt)
