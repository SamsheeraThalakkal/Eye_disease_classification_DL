
from django.urls import path,include
from Guest import views
app_name='webguest'
urlpatterns = [
    path("userRegistration/",views.userRegistration,name="userRegistration"),
    path("doctorRegistration/",views.doctorRegistration,name="doctorRegistration"),
    path("login/",views.login,name="login"),
    path("guestHome/",views.guestHome,name="guestHome")
   
]
