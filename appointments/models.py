from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.

REFERRED = (
    (0, ""), (1, "NO"), (2, "YES")
)

GENDER = (
    (0, ""), (1, "FEMALE"), (2, "MALE"), (3, "OTHER")
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

STATUS = ((0, "DRAFT"), (1, "PUBLISHED"))

STAFF = ((0, ""), (1, "NO"), (2, "YES"))


class Appointment(models.Model):
    patient_ID = models.CharField(max_length=10, null=False, blank=False, default="")
    slug = models.SlugField(max_length=200, unique=True)
    first_name = models.CharField(max_length=80, null=False, blank=False)
    last_name = models.CharField(max_length=80, null=False, blank=False)
    Gender = models.CharField(max_length=50, choices=GENDER, default="")
    referred = models.CharField(max_length=50, choices=REFERRED, default="")
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="9 AM")
    created_on = models.DateTimeField(auto_now_add=True)
    staff_member = models.ForeignKey(User, on_delete=models.CASCADE, choices=STAFF, default="")
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.user.patient_ID} | day: {self.day} | time: {self.time}"

    class Meta:
        ordering = ['patient_ID']

    def __str__(self):
        return self.patient_ID


class Comments(models.Model):
    patient_ID = models.CharField(max_length=10, null=False, blank=False, default="")
    slug = models.SlugField(max_length=200, unique=True)
    first_name = models.CharField(max_length=80, null=False, blank=False)
    last_name = models.CharField(max_length=80, null=False, blank=False)
    Gender = models.CharField(max_length=50, choices=GENDER, default="")
    referred = models.CharField(max_length=50, choices=REFERRED, default="")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    staff_member = models.ForeignKey(User, on_delete=models.CASCADE, choices=STAFF, default="")
