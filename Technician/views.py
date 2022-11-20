from django.shortcuts import render,redirect
from authentication.models import Technician
from booking.models import Booking,Treatments
from datetime import date
from django.contrib import messages
import datetime


def dashboard(request):
  if not request.session.get('username',None):
      return redirect('manager_login')
  if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
  if request.session.get('username',None) and request.session.get('type',None)=='manager':
      username=request.session['username']
      data=Technician.objects.get(username=username)
      technician_data=data.technicians_set.all()
      booked=technician_data.filter(is_available=False).count()
      print(booked)
      return render(request,"manager_dash/index.html",{"technician_data":technician_data,"manager":data,"booked":booked})
  else:
      return redirect("manager_login")


def add_technician(request):
    if not request.session.get('username',None):
      return redirect('manager_login')
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    if request.method == "GET":
        return render(request,"manager_dash/add-technician.html",{})
    else:
            technician_no = request.POST['technician_no']
            technician_type = request.POST['technician_type']
            price = request.POST['price']
            technician_image = request.FILES.get('technician_image',None)
            no_of_days_advance = request.POST['no_of_days_advance']
            start_day = request.POST['start_day']
            error = []
            if(len(technician_no)<1):
                error.append(1)
                messages.warning(request,"technician No Field must be atleast 3 digit like 100.")
            if(len(technician_type)<5):
                error.append(1)
                messages.warning(request,"Select a valid technician Type.")
            if(len(price)<=2):
                error.append(1)
                messages.warning(request,"Please enter price")
            if(len(no_of_days_advance)<1):
                error.append(1)
                messages.warning(request,"Please add valid no of days a user can book technician in advance.")
            if(len(start_day)<3):
                error.append(1)
                messages.warning(request,"Please add the starting day")
            if(not len(error)):
                manager = request.session['username']
                manager = Technician.objects.get(username=manager)
                technician = Treatments(technician_no=technician_no,technician_type=technician_type,price=price,no_of_days_advance=no_of_days_advance,start_date=datetime.datetime.strptime(start_day, "%d %B, %Y").date(),technician_image=technician_image,manager=manager)
                technician.save()
                messages.info(request,"Treatment Added Successfully")
                return redirect('/manager/dashboard1/')
            else:
                return redirect('/user/add-technician/new/')


def update_technician(request,technician_no):
    if not request.session.get('username',None):
      return redirect('manager_login')
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
        return redirect('user_dashboard')
    technician=Treatments.objects.get(technician_no=technician_no)
    if request.method == "GET":
        return render(request,"manager_dash/edit-technician.html",{"technician":technician})
    else:
        price = request.POST['price']
        no_of_days_advance = request.POST['no_of_days_advance']
        error = []
        if(len(price)<=2):
            error.append(1)
            messages.warning(request,"Please enter correct price")
        if(len(no_of_days_advance)<1):
            error.append(1)
            messages.warning(request,"Please add valid no of days a user can book technician in advance.")
        if(not len(error)):
            manager = request.session['username']
            manager = Technician.objects.get(username=manager)
            technician.price = price
            technician.no_of_days_advance = no_of_days_advance
            technician.save()
            messages.info(request,"Treatment Data Updated Successfully")
            return redirect('/manager/dashboard1/')
        else:
            return redirect('/user/add-technician/update/'+technician.technician_no,{"technician":technician})
