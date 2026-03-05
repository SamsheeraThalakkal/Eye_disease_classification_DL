from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.


def guestHome(request):
    return render(request, 'Guest/Home.html')

def userRegistration(request):
    if request.method=="POST" and request.FILES:
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        gender=request.POST.get("txt_gender")
        address=request.POST.get("txt_address")  
        photo=request.FILES.get("txt_photo")
        password=request.POST.get("txt_password")
        tbl_patient.objects.create(patient_name=name,patient_contact=contact,patient_email=email,patient_gender=gender,patient_address=address,patient_photo=photo,patient_password=password)

        return redirect('webguest:login')
    else:
        return render(request,'Guest/userRegistration.html')

def login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_pass")
        patientcount=tbl_patient.objects.filter(patient_email=email,patient_password=password).count()
        admincount=tbl_admin.objects.filter(admin_name=email,admin_password=password).count()
        doctorcount=tbl_doctor.objects.filter(doctor_email=email,doctor_password=password).count()
       
        if patientcount > 0:
            userdata=tbl_patient.objects.filter(patient_email=email,patient_password=password).first()
            request.session['uid']=userdata.id
            return redirect('webpatient:userHome')
        elif admincount > 0:
            admindata=tbl_admin.objects.filter(admin_name=email,admin_password=password).first()
            request.session['aid']=admindata.id
            return redirect('webadmin:adminHome')
        elif doctorcount > 0:
            doctordata=tbl_doctor.objects.filter(doctor_email=email,doctor_password=password).first()
            request.session['did']=doctordata.id
            return redirect('webdoctor:doctorHome')
        else:
            msg="Invalid credentials or pending verification!!"
            return render(request,'Guest/Login.html',{'msg':msg})
    else:
        return render(request,'Guest/Login.html')
