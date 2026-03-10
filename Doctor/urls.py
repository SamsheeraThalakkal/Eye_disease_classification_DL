from django.urls import path
from Doctor import views

app_name = 'webdoctor'

urlpatterns = [
    path('doctorHome/', views.doctorHome, name='doctorHome'),
    path('addAvailability/', views.addAvailability, name='addAvailability'),
    path('diagnose/', views.diagnose, name='diagnose'),
    path('editAvailability/<int:lid>/', views.editAvailability, name='editAvailability'),
    path('delAvailability/<int:lid>/', views.delAvailability, name='delAvailability'),
]
