from django.urls import path
from Doctor import views

app_name = 'webdoctor'

urlpatterns = [
    path('doctorHome/', views.doctorHome, name='doctorHome'),
    path('addLocation/', views.addLocation, name='addLocation'),
    path('deleteLocation/<int:id>/', views.deleteLocation, name='deleteLocation'),
]
