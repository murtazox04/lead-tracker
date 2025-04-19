import uuid
from django.db import models


class Lead(models.Model):
    class LeadState(models.TextChoices):
        PENDING = "PENDING", "Pending"
        REACHED_OUT = "REACHED_OUT", "Reached Out"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    resume = models.FileField(upload_to="resumes/")

    state = models.CharField(
        max_length=20, choices=LeadState.choices, default=LeadState.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
