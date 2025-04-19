import pytest
from leads.models import Lead
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_public_lead_create_view():
    client = APIClient()

    with open("leads/tests/resumes/MurtazoXurramovResume.pdf", "rb") as f:
        data = {
            "first_name": "View",
            "last_name": "Test",
            "email": "viewtest@example.com",
            "resume": f,
        }
        response = client.post("/api/leads/create/", data, format="multipart")

    assert response.status_code == 201
    assert Lead.objects.count() == 1


@pytest.mark.django_db
def test_authenticated_lead_list_view():
    user = User.objects.create_user(username="admin", password="password123")
    client = APIClient()
    client.login(username="admin", password="password123")

    Lead.objects.create(
        first_name="List",
        last_name="Test",
        email="list@example.com",
        resume="resumes/list.pdf",
    )

    response = client.get("/api/leads/")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["email"] == "list@example.com"


@pytest.mark.django_db
def test_mark_lead_as_reached_out():
    user = User.objects.create_user(username="admin2", password="password456")
    client = APIClient()
    client.login(username="admin2", password="password456")

    lead = Lead.objects.create(
        first_name="Patch",
        last_name="Test",
        email="patch@example.com",
        resume="resumes/patch.pdf",
    )

    url = f"/api/leads/{lead.id}/mark-reached/"
    response = client.patch(url)

    assert response.status_code == 200

    lead.refresh_from_db()
    assert lead.state == Lead.LeadState.REACHED_OUT
