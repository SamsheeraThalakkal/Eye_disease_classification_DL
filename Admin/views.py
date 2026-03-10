from django.shortcuts import render, redirect
from Admin.models import *
from Guest.models import *
# Create your views here.

def adminHome(request):
    return render(request,'Admin/adminHome.html')

def manageDoctors(request):
    return render(request, 'Admin/manageDoctors.html')

def addDoctor(request):
    if request.method == "POST":
        tbl_doctor.objects.create(
            doctor_name=request.POST.get("txt_name"),
            doctor_contact=request.POST.get("txt_contact"),
            doctor_email=request.POST.get("txt_email"),
            doctor_gender=request.POST.get("gender"),
            doctor_address=request.POST.get("txt_address"),
            doctor_photo=request.FILES.get("file_photo"),
            doctor_password=request.POST.get("txt_password")
        )
        return redirect("webadmin:viewDoctors")
    else:
        doc = tbl_doctor.objects.all()
        return render(request,'Admin/viewDoctor.html', {'doc': doc})

def delDoctor(request, did):
    tbl_doctor.objects.get(id=did).delete()
    return redirect("webadmin:viewDoctors")

def editDoctor(request, eid):
    editData = tbl_doctor.objects.get(id=eid)
    
    if request.method == "POST":
        editData.doctor_name = request.POST.get("txt_name")
        editData.doctor_contact = request.POST.get("txt_contact")
        editData.doctor_email = request.POST.get("txt_email")
        editData.doctor_gender = request.POST.get("gender")
        editData.doctor_address = request.POST.get("txt_address")
        editData.specialization = request.POST.get("txt_specialization")
        if request.FILES.get("file_photo"):
            editData.doctor_photo = request.FILES.get("file_photo")
        editData.doctor_password = request.POST.get("txt_password")
        editData.save()
        return redirect("webadmin:doctorRegistration")
    else:
        return render(request,'Admin/doctorRegistration.html', {'editData': editData})



def doctorRegistration(request):
    if request.method=="POST" and request.FILES:
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        gender=request.POST.get("gender")
        specialization=request.POST.get("txt_specialization")
        address=request.POST.get("txt_address")  
        photo=request.FILES.get("file_photo")
        password=request.POST.get("txt_password")
        tbl_doctor.objects.create(doctor_name=name,doctor_contact=contact,doctor_email=email,doctor_gender=gender,doctor_address=address,specialization=specialization,doctor_photo=photo,doctor_password=password)

        return redirect('webadmin:doctorRegistration')
    else:
        return render(request,'Admin/doctorRegistration.html')

def viewPatients(request):
    patients = tbl_patient.objects.all()
    return render(request, 'Admin/viewPatients.html', {'patients': patients})

def viewDoctors(request):
    doctors = tbl_doctor.objects.all()
    return render(request, 'Admin/viewDoctor.html', {'doctors': doctors})

def delPatient(request, pid):
    tbl_patient.objects.get(id=pid).delete()
    return redirect("webadmin:viewPatients")

def editPatient(request, eid):
    editData = tbl_patient.objects.get(id=eid)
    
    if request.method == "POST":
        editData.patient_name = request.POST.get("txt_name")
        editData.patient_contact = request.POST.get("txt_contact")
        editData.patient_email = request.POST.get("txt_email")
        editData.patient_gender = request.POST.get("txt_gender")        
        editData.patient_address = request.POST.get("txt_address")
        if request.FILES.get("file_photo"):
            editData.patient_photo = request.FILES.get("file_photo")
        editData.patient_password = request.POST.get("txt_password")
        editData.save()
        return redirect("webadmin:viewPatients")
    else:
        return render(request,'Guest/userRegistration.html', {'editData': editData})