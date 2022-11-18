from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from salon.forms import UserRegisterForm, TechnicianRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django import forms
from .models import User, Technician,Treatment,TreatmentStatus, TreatmentType


# Create your views here.
def homepage(request):
    return render(request,"salon/index.html")

def about(request):
    return render(request,"salon/about.html")
    treatment_types = TreatmentType.objects.all()
    treatment = Treatment.objects.all()
    treatment_status = TreatmentStatus.objects.all()
    context = {"treatments": treatment_types,"treatment_status":treatment_status,"treatment_no":treatment}

def treatments(request):
    return render(request, "salon/treatments.html", context)

def treatments_detailed_view(request, treatment_id):
    treatment_detail = get_object_or_404(TreatmentType, pk=treatment_id)
    return render(request, "salon/treatments_views.html",{"treatment": treatment_detail,"treatments": treatment_types,"treatment_no":treatment})

def booking(request,treatment_id):
    treatment_detail = get_object_or_404(TreatmentType, pk=treatment_id)
    return render(request, "salon/booking.html",{"treatment": treatment_detail,"treatments": treatment_types,"treatment_no":treatment})