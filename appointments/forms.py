from django import forms
from .models import Appointment, Comment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('patient_ID', 'author', 'full_name', 'gender', 'address', 'appointment_number', 'appointment_notes', 'date', 'status')

        widgets = {
            'patient_ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a 10 digit patient ID'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Please enter the Patient's full name"}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'appointment_number': forms.Select(attrs={'class': 'form-control'}),
            'appointment_notes': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
