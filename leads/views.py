from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

from .models import Lead
from .serializers import LeadCreateSerializer, LeadListSerializer


class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadCreateSerializer
    permission_classes = []  # Public
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer: LeadCreateSerializer):
        lead = serializer.save()
        self.send_email_notifications(lead)

    def send_email_notifications(self, lead):
        subject_user = "Thank you for your submission"
        message_user = render_to_string(
            "emails/user_confirmation.html",
            {
                "first_name": lead.first_name,
            },
        )
        email_user = EmailMessage(
            subject_user, message_user, settings.DEFAULT_FROM_EMAIL, [lead.email]
        )
        email_user.content_subtype = "html"
        email_user.send()

        subject_admin = "New Lead Submitted"
        message_admin = render_to_string(
            "emails/notify_admin.html",
            {
                "first_name": lead.first_name,
                "last_name": lead.last_name,
                "email": lead.email,
            },
        )
        email_admin = EmailMessage(
            subject_admin,
            message_admin,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ATTORNEY_EMAIL],
        )
        email_admin.content_subtype = "html"
        email_admin.send()


class LeadListView(generics.ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadListSerializer
    permission_classes = [permissions.IsAuthenticated]


class LeadMarkReachedOutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            lead = Lead.objects.get(pk=pk)
        except Lead.DoesNotExist:
            return Response({"detail": "Lead not found."}, status=404)

        lead.state = Lead.LeadState.REACHED_OUT
        lead.save()
        return Response({"detail": "Lead marked as REACHED_OUT."})
