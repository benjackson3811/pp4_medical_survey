from django.shortcuts import render
from django.views import generic
from .models import Appointment, Comment
from .forms import AppointmentForm

# index form styling from from https://www.youtube.com/watch?v=6-XXvUENY_8


class AppointmentList(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class AddAppointment(generic.CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = "add_appointment.html"


