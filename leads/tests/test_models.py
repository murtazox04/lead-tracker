import pytest
from leads.models import Lead


@pytest.mark.django_db
def test_lead_model_defaults():
    lead = Lead.objects.create(
        first_name="Test",
        last_name="Model",
        email="model@example.com",
        resume="resumes/test.pdf",
    )

    assert lead.pk is not None
    assert lead.state == Lead.LeadState.PENDING
    assert str(lead) == "Test Model (model@example.com)"
