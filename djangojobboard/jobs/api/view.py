from django.conf import settings
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from djangojobboard.jobs.models import Job
from .serializers import JobSerializer

import stripe

stripe.api_key = 'sk_test_51HVHJwGjLUpjNrZJu3vgdjlUm9iauNKb7KApNRI8MwMBjgRQZGITjUKQh5kRGjU5TvSekakytNwDXWw1HV3hQ1AZ00RqM8jzeG'
stripe.api_key = settings.STRIPE_SECRET_KEY




class JobListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.filter(available=True)
    
    
class JobCreateView(CreateAPIView):
    #permission_classes = [isAuthenticated]
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class JobDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.all()
    
     
class JobUpdateView(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.filter(available=True)
    

class JobDeleteView(DestroyAPIView):
    permission_classes = [AllowAny]
    def get_queryset(self):
        return Job.objects.all()
    
    
class CreatePaymentView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            intent = stripe.PaymentIntent.create(
                amount=1000,
                currency="usd",
                automatic_payment_methods={
                    "enabled": True,
                },
                metadata={
                    "job_id": request.data["job_id"]
                }
            )
            return Response({"clientSecret": intent["client_secret"]})
        except Exception as e:
            return Response({"error": str(e)}, status=403)
        