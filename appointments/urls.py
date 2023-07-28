from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('add_appointment', views.appointment, name='appointment'),
    path('appointment-submit', views.appointmentSubmit, name='appointmentSubmit'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<int:id>', views.userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel', views.staffPanel, name='staffPanel'),
]
