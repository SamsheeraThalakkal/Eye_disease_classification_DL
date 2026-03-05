from django.urls import path
from Doctor import views

app_name = 'webdoctor'

urlpatterns = [
    path('doctorHome/', views.doctorHome, name='doctorHome'),
    path('addAvailability/', views.addAvailability, name='addAvailability'),
]
