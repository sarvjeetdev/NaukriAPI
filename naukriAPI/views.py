# views.py
from rest_framework import generics
from .models import NaukriJobs
from .serializers import NaukriJobsSerializer

# GET request to list jobs, POST request to add a new job
class NaukriJobsListCreateView(generics.ListCreateAPIView):
    queryset = NaukriJobs.objects.all()
    serializer_class = NaukriJobsSerializer
