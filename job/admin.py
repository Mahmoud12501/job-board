from django.contrib import admin
from .models import Job,Category,Location,Applicants
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class JobModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Job,JobModelAdmin)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Applicants)