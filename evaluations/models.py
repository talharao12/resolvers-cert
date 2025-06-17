from django.db import models
import uuid

class QualificationEvaluation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    reference_id = models.IntegerField(unique=True)
    holder_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    qualification_name = models.CharField(max_length=100)
    major_specialization = models.CharField(max_length=100)
    awarding_year = models.IntegerField()
    country_of_education = models.CharField(max_length=100)
    awarding_institution = models.CharField(max_length=200)
    institution_status = models.CharField(max_length=100)
    qualification_type = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    evaluation_notes = models.TextField()

    def __str__(self):
        return f"{self.holder_name} - {self.qualification_name} ({self.awarding_year})"