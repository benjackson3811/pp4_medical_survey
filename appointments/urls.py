from . import views
from django.urls import path

urlpatterns = [
    path('', views.AppointmentList.as_view(), name='home'),
    path('add_appointment', views.appointment_form, name='add_appointment')
]
