from django.shortcuts import render
from django.views import generic
from .models import Appointment, Comment

# index function from https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page


def index(request):

    num_appointments = Appointment.objects.all().count()

    appointment = {
        'num_appointments': num_appointments,
        'num_comments': num_comments,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', {'appointment': appointment})

class AppointmentList(generic.ListView):
    model = Appointment
    queryset = Appointment.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 12
