from django.contrib import admin
from .models import Appointment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Appointment)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('patient_ID', 'full_name', 'status', 'created_on', 'day', 'appointment_number')
    search_fields = ('patient_ID', 'full_name', 'appointment_number')
    list_filter = ('status', 'created_on', 'updated_on')
    summernote_fields = ('content',)

