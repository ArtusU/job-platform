from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from djangojobboard.jobs.models import Job
from .serializers import JobSerializer


class JobListView(ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.filter(available=True)
    
    
class JobCreateView(CreateAPIView):
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class JobDetailView(RetrieveAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.all()
    
     
class JobUpdateView(UpdateAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.filter(available=True)
    

class JobDeleteView(DestroyAPIView):
    def get_queryset(self):
        return Job.objects.all()