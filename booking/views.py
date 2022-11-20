from django.shortcuts import render,redirect
from .models import *
from authentication.models import Customer
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime, timedelta

def index(request):
    return render(request,'booking/index.html',{})

def booking(request):
    weekdays = validWeekday(22)
    # only show day not booked out
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service == None:
            messages.success(request, "Please select a service!")
            return redirect('booking')

        request.session['day'] = day
        request.session['service'] = service

        return redirect('bookingSubmit')

    return render(request, 'booking.html', {
        'weekdays':weekdays,
        'validateWeekdays':validateWeekdays,
    })

def contact(request):
    if request.method=="GET":
        return render(request,"contact/contact.html",{})
    else:
        username=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        data=Contact(name=username,email=email,message=message)
        data.save()
        return render(request,"contact/contact.html",{'message':'Thank you for contacting us.'})

#def book(request):
#    if request.method=="POST":
#        start_date=request.POST['start_date']
#        end_date=request.POST['end_date']
#        request.session['start_date']=start_date
#        request.session['end_date']=end_date
#        start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
#        end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
#        no_of_days=(end_date-start_date).days
#        data=Treatments.objects.filter(is_available=True,no_of_days_advance__gte=no_of_days,start_date__lte=start_date)
#        request.session['no_of_days']=no_of_days
#        return render(request,'booking/book.html',{'data':data})
#    else:
#        return redirect('index')

#def book_now(request,id):
#    if request.session.get("username",None) and request.session.get("type",None)=='customer':
#        if request.session.get("no_of_days",1):
#            no_of_days=request.session['no_of_days']
#            start_date=request.session['start_date']
#            end_date=request.session['end_date']
#            request.session['technician_no']=id
#            data=Treatments.objects.get(treatment_no=id)
#            bill=data.price*int(no_of_days)
#            request.session['bill']=bill
#            technician=data.manager.username
#            return render(request,"booking/book-now.html",{"no_of_days":no_of_days,"data":data,"bill":bill,"technician":technician,"start":start_date,"end":end_date})
#        else:
#            return redirect("index")
#    else:
#        next="book-now/"+id
#        return redirect('user_login')
        
#def book_confirm(request):
#    treatment_no=request.session['technician_no']
#    start_date=request.session['start_date']
#    end_date=request.session['end_date']
#    username=request.session['username']
#    user_id=Customer.objects.get(username=username)
#    treatment=Treatments.objects.get(treatment_no=treatment_no)
#    amount=request.session['bill']
#    start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
#    end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
#    data=Booking(technician_no=technician,start_day=start_date,end_day=end_date,amount=amount,user_id=user_id)
#    data.save()
#    treatment.is_available=False
#    treatment.save()
#    del request.session['start_date']
#    del request.session['end_date']
#    del request.session['bill']
#    del request.session['treatment_no']
#    messages.info(request,"treatment has been successfully booked")
#    return redirect('user_dashboard')

#def cancel_treatment(request,id):
#    data=Booking.objects.get(id=id)
#    treatment=data.treatment_no
#    treatment.is_available=True
#    treatment.save()
#    data.delete()
#    return HttpResponse("Booking Cancelled Successfully")

#def delete_treatment(request,id):
#    data=Treatments.objects.get(id=id)
#    manager=data.manager.username
#    if manager==request.session['username']:
#        data.delete()
#        return HttpResponse("You have deleted the treatment successfully")
#    else:
#        return HttpResponse("Invalid Request")
