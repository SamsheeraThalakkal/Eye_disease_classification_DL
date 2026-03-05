
from django.urls import path,include
from Guest import views
app_name='webguest'
urlpatterns = [
    path("userRegistration/",views.userRegistration,name="userRegistration"),
    path("login/",views.login,name="login"),
    path("",views.guestHome,name="guestHome")
   
]
