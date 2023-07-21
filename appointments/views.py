from django.shortcuts import render
import django.views import generic
.models import Appointment

class AppointmentList(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.filter(status=1).order_by('-created_on')
    template_name ='index.html'
    paginate_by = 10
