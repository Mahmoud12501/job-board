from django.urls import path,include
from . import views
from . import api

app_name='job'

urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add_job',views.add_job,name='add_job'),
    path('<str:slug>',views.job_detail,name='job_detail'),
    
    # api
    path('api/list',api.joblist_api,name='joblist_api'),
]