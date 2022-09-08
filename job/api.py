# same views but return jason
from .models import Job
from .serializer import JobSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def joblist_api(request):
    job_list=Job.objects.all()
    data=JobSerializers(job_list,many=True).data
    return Response({'data':data})