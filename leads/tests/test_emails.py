import pytest
from django.core import mail
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_lead_creation_sends_emails(settings):
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

    client = APIClient()
    data = {
        "first_name": "Murtazo",
        "last_name": "Xurramov",
        "email": "murtazox04@gmail.com",
    }

    with open("leads/tests/resumes/MurtazoXurramovResume.pdf", "rb") as f:
        data["resume"] = f
        response = client.post("/api/leads/create/", data, format="multipart")

    assert response.status_code == 201
    assert len(mail.outbox) == 2
    assert "Thank you" in mail.outbox[0].subject
    assert "New Lead" in mail.outbox[1].subject
