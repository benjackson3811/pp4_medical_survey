from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.


GENDER = (
    ("", ""), ("FEMALE", "FEMALE"), ("MALE", "MALE"), ("OTHER", "OTHER")
)

TIME_CHOICES = (
    ("9 AM", "9 AM"),
    ("9:30 PM", "9:30 AM"),
    ("10 PM", "10 PM"),
    ("10:30 AM", "10:30 AM"),
    ("11 PM", "11 AM"),
    ("11:30 AM", "11:30 AM"),
    ("12 PM", "12 PM"),
    ("12:30 PM", "12:30 PM"),
    ("1 PM", "1 PM"),
    ("1:30 PM", "1:30 PM"),
)

STATUS = (
    (0, ""),
    (1, "Just Recruited"),
    (2, "Completed First Appointment"),
    (3, "Completed Second Appointment")
)

APPOINTMENT_NUMBER = (
    ("Inital Appointment", "Inital Appointment"),
    ("Follow Up Appointment", "Follow Up Appointment"),
    ("Final Results", "Final Results"),
    )


class Appointment(models.Model):
    patient_ID = models.CharField(max_length=80, null=False, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="appointment_number", null=True, blank=True)
    full_name = models.CharField(max_length=80, null=False, blank=False)
    gender = models.CharField(max_length=10, choices=GENDER, default="")
    address = models.CharField(max_length=200, null=False, default="")
    appointment_number = models.CharField(
        max_length=50, choices=APPOINTMENT_NUMBER, default="")
    updated_on = models.DateTimeField(auto_now=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(
        max_length=10, choices=TIME_CHOICES, default="9 AM")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['patient_ID']

    def __str__(self):
        return f"{self.patient_ID}, {self.full_name}"

    def update_appointment(ModelAdmin, request, queryset):
        queryset.update(status="p")


