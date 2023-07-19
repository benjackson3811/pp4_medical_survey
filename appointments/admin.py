from django.contrib import admin
from .models import Appointment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Appointment)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('patient_ID',)}
    summernote_fields = ('content',)
