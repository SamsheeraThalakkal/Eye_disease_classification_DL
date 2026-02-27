from django.shortcuts import render, redirect
from Guest.models import tbl_doctor

# Create your views here.

def adminHome(request):
    return render(request,'Admin/adminHome.html')

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
        return redirect("webamin:addDoctor")
    else:
        doc = tbl_doctor.objects.all()
        return render(request,'Admin/addDoctor.html', {'doc': doc})

def delDoctor(request, did):
    tbl_doctor.objects.get(id=did).delete()
    return redirect("webamin:addDoctor")

def editDoctor(request, eid):
    editData = tbl_doctor.objects.get(id=eid)
    doc = tbl_doctor.objects.all()
    if request.method == "POST":
        editData.doctor_name = request.POST.get("txt_name")
        editData.doctor_contact = request.POST.get("txt_contact")
        editData.doctor_email = request.POST.get("txt_email")
        editData.doctor_gender = request.POST.get("gender")
        editData.doctor_address = request.POST.get("txt_address")
        if request.FILES.get("file_photo"):
            editData.doctor_photo = request.FILES.get("file_photo")
        editData.doctor_password = request.POST.get("txt_password")
        editData.save()
        return redirect("webamin:addDoctor")
    else:
        return render(request,'Admin/addDoctor.html', {'editData': editData, 'doc': doc})

def verifyDoctor(request):
    pending = tbl_doctor.objects.filter(doctor_status=0)
    accepted = tbl_doctor.objects.filter(doctor_status=1)
    rejected = tbl_doctor.objects.filter(doctor_status=2)
    return render(request, 'Admin/verifyDoctor.html', {'pending': pending, 'accepted': accepted, 'rejected': rejected})

def acceptDoctor(request, aid):
    doctor = tbl_doctor.objects.get(id=aid)
    doctor.doctor_status = 1
    doctor.save()
    return redirect('webadmin:verifyDoctor')

def rejectDoctor(request, rid):
    doctor = tbl_doctor.objects.get(id=rid)
    doctor.doctor_status = 2
    doctor.save()
    return redirect('webadmin:verifyDoctor')