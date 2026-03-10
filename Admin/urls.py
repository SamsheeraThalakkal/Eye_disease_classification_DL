
from django.urls import path,include
from Admin import views

app_name='webadmin'

urlpatterns = [
    
    path("adminHome/",views.adminHome,name="adminHome"),
    path("addDoctor/",views.addDoctor,name="addDoctor"),
    path("delDoctor/<int:did>",views.delDoctor,name="delDoctor"),
    path("editDoctor/<int:eid>",views.editDoctor,name="editDoctor"),
    path("viewPatients/",views.viewPatients,name="viewPatients"),
    path("doctorRegistration/",views.doctorRegistration,name="doctorRegistration"),
    path("viewDoctors/",views.viewDoctors,name="viewDoctors"),
    path('manageDoctors/', views.manageDoctors, name='manageDoctors'),
    path("editPatient/<int:eid>",views.editPatient,name="editPatient"),
    path("delPatient/<int:pid>",views.delPatient,name="delPatient"),
]
