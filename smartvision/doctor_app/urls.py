from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='doctor_register'),
    path('login/', views.login, name='doctor_login'),
]
