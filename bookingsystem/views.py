from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from salon.forms import UserRegisterForm, TechnicianRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django import forms
from .models import User, Technician, Treatment, TreatmentStatus, TreatmentType


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

# Authorization
def admin_create(request):
    if request.method == “POST”:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, “Your account has been created successfully! You are now able to log in”)
            return redirect("admin-login")
        else:
            form = UserRegisterForm()
            return render(request, "salon/register.html", {"form": form})

def register_technician(request):
    if request.method == “POST”:
        form = TechnicianRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get("first_name")
            messages.success(request, “Your account has been created successfully as a Technician! You are now able to log in”)
            return redirect("admin-login")
        else:
            form = TechnicianRegisterForm()
            return render(request, "salon/register_Reception.html", {"form": form})

@login_required
def profile(request):
    return render(request, "salon/profile.html")

@login_required
def dashboard(request):
    return render(request, "salon/dashboard.html", {"dash": "This is the dashboard"})

def admin_list(request):
    salon_admin_list = User.objects.all()
    return render(request, "salon/admin_list.html", {"admin_lists": salon_admin_list})

def show_admin(request, uuid):
    display_admin = Technician.objects.get(uuid(uuid))
    return render(request, "salon/show_admin.html", {"show_admin": display_admin})