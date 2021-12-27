from django.conf import settings
from django.urls import path
from djangojobboard.jobs.api.view import JobListView, JobCreateView, JobUpdateView, JobDeleteView, JobDetailView, CreatePaymentView
from rest_framework.routers import DefaultRouter, SimpleRouter

from djangojobboard.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"

urlpatterns = [
    path("jobs/", JobListView.as_view()),
    path("jobs/<pk>/", JobDetailView.as_view()),
    path("jobs/<pk>/update/", JobUpdateView.as_view()),
    path("jobs/<pk>/delete/", JobDeleteView.as_view()),
    path("create-job/", JobCreateView.as_view()),
    path("payments/create-payment/", CreatePaymentView.as_view()),
]
urlpatterns += router.urls
