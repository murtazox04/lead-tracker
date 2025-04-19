from django.urls import path
from .views import LeadCreateView, LeadListView, LeadMarkReachedOutView

urlpatterns = [
    path("", LeadListView.as_view(), name="lead-list"),
    path("create/", LeadCreateView.as_view(), name="lead-create"),
    path(
        "<uuid:pk>/mark-reached/", LeadMarkReachedOutView.as_view(), name="lead-reach"
    ),
]
