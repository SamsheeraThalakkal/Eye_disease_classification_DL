from django.shortcuts import render, redirect
from Doctor.models import *
from Admin.models import *

def doctorHome(request):
    if 'did' in request.session:
        doctor = tbl_doctor.objects.get(id=request.session['did'])
        return render(request,'Doctor/doctorHome.html', {'doctor': doctor})
    else:
        return redirect('webguest:login')

def addAvailability(request):
    if 'did' in request.session:
        doctor = tbl_doctor.objects.get(id=request.session['did'])
        locations = tbl_location.objects.filter(doctor=doctor).order_by('available_date', 'start_time')
        
        if request.method == "POST":
            available_date = request.POST.get("txt_date")
            start_time = request.POST.get("txt_start")
            end_time = request.POST.get("txt_end")
            
            tbl_location.objects.create(
                available_date=available_date,
                start_time=start_time,
                end_time=end_time,
                doctor=doctor
            )
            return redirect('webdoctor:addAvailability')
            
        return render(request, 'Doctor/addAvailability.html', {'locations': locations})
    else:
        return redirect('webguest:login')

