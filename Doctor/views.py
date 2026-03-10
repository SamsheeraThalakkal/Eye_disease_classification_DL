from django.shortcuts import render, redirect
from Doctor.models import *
from Admin.models import *
import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from django.shortcuts import render
from django.conf import settings

import cv2
import numpy as np
from PIL import Image
import torch


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


import os
import cv2
import torch
import torch.nn as nn
import numpy as np
from PIL import Image
from torchvision import models, transforms
from django.shortcuts import render
from django.conf import settings


# ===== MODEL LOAD =====
MODEL_PATH = os.path.join(settings.BASE_DIR, "Doctor", "model", "efficientnet_b3_odir5k_binocular.pth")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# CHANGED → 8 classes (same as trained model)
target_cols = ['Normal','Diabetes','Glaucoma','Cataract','AMD','Hypertension','Myopia','Others']

model = models.efficientnet_b3(weights=None)
in_features = model.classifier[1].in_features

# CHANGED → output = 8
model.classifier[1] = nn.Linear(in_features, 8)

model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])


# ===== PREPROCESS FUNCTION =====
def clean_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (512,512))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        x,y,w,h = cv2.boundingRect(contours[0])
        img = img[y:y+h, x:x+w]

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)

    return img


# ===== VIEW =====
def diagnose(request):
    context = {}

    if request.method == "POST":

        left_file = request.FILES['left_image']
        right_file = request.FILES['right_image']

        left_path = os.path.join(settings.MEDIA_ROOT, left_file.name)
        right_path = os.path.join(settings.MEDIA_ROOT, right_file.name)

        with open(left_path, 'wb+') as f:
            for chunk in left_file.chunks():
                f.write(chunk)

        with open(right_path, 'wb+') as f:
            for chunk in right_file.chunks():
                f.write(chunk)

        # Clean images
        left_img = clean_image(left_path)
        right_img = clean_image(right_path)

        # ===== Vertical Fusion (same as training) =====
        w, h = left_img.size
        fused = Image.new('RGB', (w, h*2))
        fused.paste(left_img, (0,0))
        fused.paste(right_img, (0,h))

        fused = transform(fused).unsqueeze(0).to(device)

        # ===== Prediction =====
        with torch.no_grad():
            output = model(fused)
            probs = torch.sigmoid(output)
            preds = (probs > 0.5).int().cpu().numpy()[0]

        predicted_labels = []
        for i in range(len(preds)):
            if preds[i] == 1:
                predicted_labels.append(target_cols[i])

        if not predicted_labels:
            predicted_labels.append("No Disease Detected")

        context['prediction'] = ", ".join(predicted_labels)

    return render(request, "Doctor/diagnose.html", context)

def editAvailability(request, lid):
    editData = tbl_location.objects.get(id=lid)
    
    if request.method == "POST":
        editData.available_date = request.POST.get("txt_date")
        editData.start_time = request.POST.get("txt_start")
        editData.end_time = request.POST.get("txt_end")
        editData.save()
        return redirect("webdoctor:addAvailability")
    else:
        return render(request,'Doctor/addAvailability.html', {'editData': editData})

def delAvailability(request, lid):

    tbl_location.objects.get(id=lid).delete()
    return redirect("webdoctor:addAvailability")