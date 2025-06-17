from django.contrib import admin
from .models import QualificationEvaluation

@admin.register(QualificationEvaluation)
class QualificationEvaluationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'reference_id',
        'holder_name',
        'qualification_name',
        'major_specialization',
        'awarding_year',
        'awarding_institution',
        'country_of_education',
    )
    search_fields = ('holder_name', 'reference_id', 'qualification_name', 'awarding_institution')
    list_filter = ('awarding_year', 'country_of_education', 'qualification_type')
