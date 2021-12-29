from rest_framework.permissions import BasePermission


class IsJobOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        job = obj
        return job.user == request.user