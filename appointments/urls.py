from . import views
from django.urls import path

urlpatterns = [
    path('', views.AppointmentList.as_view(), name='index'),
    path('add_appointment/',views.AddAppointment.as_view(), name='add_appointment')
]
