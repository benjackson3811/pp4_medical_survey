from django.contrib import admin
from .models import Appointment, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Appointment)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('patient_ID', 'slug', 'full_name', 'status', 'created_on', 'day', 'appointment_number')
    search_fields = ('patient_ID', 'full_name', 'appointment_number')
    prepopulated_fields = {'slug': ('patient_ID',)}
    list_filter = ('status', 'created_on', 'updated_on')
    summernote_fields = ('content',)


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):

    list_display = ('patient_ID', 'slug', 'full_name', 'created_on', 'appointment_number')
    search_fields = ('patient_ID', 'full_name', 'status', 'gender')
    prepopulated_fields = {'slug': ('patient_ID',)}
    list_filter = ('status', 'created_on', 'appointment_number')
    summernote_fields = ('content',)
    actions = ['status']

    def approve_comments(self, request, queryset):
        queryset.update(status=True)

    class patient_IDInstanceAdmin(admin.ModelAdmin):
        list_filter = ('patient_ID', 'full_name', 'day', 'created_on')

