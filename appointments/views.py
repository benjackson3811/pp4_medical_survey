from django.shortcuts import render
from django.views import generic
from .models import Appointment, Comment
from .forms import AppointmentForm

# form function taken from from https://www.csestack.org/create-html-form-insert-data-database-django/
# index form styling from from https://www.youtube.com/watch?v=6-XXvUENY_8


class AppointmentList(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6



def appointment_form(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AppointmentForm()
    return render(request, 'add_appointment.html', {'form': form})

