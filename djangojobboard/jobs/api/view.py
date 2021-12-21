from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from djangojobboard.jobs.models import Job
from .serializers import JobSerializer


class JobListView(ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.filter(available=True)