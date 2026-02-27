from django.shortcuts import render, redirect
from Doctor.models import tbl_location
from Guest.models import tbl_doctor

def doctorHome(request):
    if 'did' in request.session:
        doctor = tbl_doctor.objects.get(id=request.session['did'])
        return render(request,'Doctor/doctorHome.html', {'doctor': doctor})
    else:
        return redirect('webguest:login')

def addLocation(request):
    if 'did' in request.session:
        doctor = tbl_doctor.objects.get(id=request.session['did'])
        locations = tbl_location.objects.filter(doctor=doctor).order_by('available_date', 'start_time')
        
        if request.method == "POST":
            location_name = request.POST.get("txt_location")
            available_date = request.POST.get("txt_date")
            start_time = request.POST.get("txt_start")
            end_time = request.POST.get("txt_end")
            
            tbl_location.objects.create(
                location_name=location_name,
                available_date=available_date,
                start_time=start_time,
                end_time=end_time,
                doctor=doctor
            )
            return redirect('webdoctor:addLocation')
            
        return render(request, 'Doctor/addLocation.html', {'locations': locations})
    else:
        return redirect('webguest:login')

def deleteLocation(request, id):
    if 'did' in request.session:
        tbl_location.objects.get(id=id).delete()
        return redirect('webdoctor:addLocation')
    else:
        return redirect('webguest:login')
