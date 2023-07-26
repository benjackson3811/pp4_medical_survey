from django import forms
from .models import Appointment, Comment


class AppointmentForm(forms.ModelForm):

    """Class to create an appointment form"""

    class Meta:
        """ Class to add the form body to the form based on the appointment"""
        """ model"""
        
        model = Appointment
        fields = ('patient_ID', 'author', 'full_name', 'gender', 'address', 
        'appointment_number', 'appointment_notes', 'day', 'status')

        widgets = {
            'patient_ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a 10 digit patient ID'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Please enter the Patient's full name"}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'appointment_number': forms.Select(attrs={'class': 'form-control'}),
            'appointment_notes': forms.Textarea(attrs={'class': 'form-control'}),
            'day': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
