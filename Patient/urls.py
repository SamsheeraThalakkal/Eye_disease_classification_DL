
from django.urls import path,include
from Patient import views

app_name='webpatient'
urlpatterns = [
  
    path("userHome/",views.userHome,name="userHome"),
   
]
