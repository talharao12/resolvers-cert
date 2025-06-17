from django.shortcuts import render
from django.http import Http404
from .models import QualificationEvaluation
import uuid

def verify_qualification(request, reference_uuid):
    try:
        qualification = QualificationEvaluation.objects.get(id=reference_uuid)
    except QualificationEvaluation.DoesNotExist:
        raise Http404("Qualification not found")
    
    return render(request, 'qualification_detail1.html', {'qualification': qualification})
