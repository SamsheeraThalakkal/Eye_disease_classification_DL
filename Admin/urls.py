
from django.urls import path,include
from Admin import views

app_name='webadmin'

urlpatterns = [
    
    path("adminHome/",views.adminHome,name="adminHome"),
    path("addDoctor/",views.addDoctor,name="addDoctor"),
    path("delDoctor/<int:did>",views.delDoctor,name="delDoctor"),
    path("editDoctor/<int:eid>",views.editDoctor,name="editDoctor"),
    # path("verifyDoctor/",views.verifyDoctor,name="verifyDoctor"),
    path("viewUser/",views.viewUser,name="viewUser"),
    path("doctorRegistration/",views.doctorRegistration,name="doctorRegistration"),
    path("acceptDoctor/<int:aid>",views.acceptDoctor,name="acceptDoctor"),
    path("rejectDoctor/<int:rid>",views.rejectDoctor,name="rejectDoctor"),
]
