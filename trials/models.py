from django.db import models
from django.contrib.auth.models import User


class ClinicalTrial(models.Model):

    PHASE_CHOICES = [
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    phase = models.CharField(max_length=20, choices=PHASE_CHOICES)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    start_date = models.DateField()
    end_date = models.DateField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="clinical_trials"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # newest first automatically

    def __str__(self):
        return self.title
