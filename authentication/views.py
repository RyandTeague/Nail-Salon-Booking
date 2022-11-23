from django.shortcuts import render, redirect
from .models import Customer, Technician
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.core.mail import send_mail







#def user_login(request):
#    if request.session.get('username', None) and request.session.get('type', None)=='customer':
#        return redirect('user_dashboard')
#    if request.session.get('username', None) and request.session.get('type', None)=='manager':
#        return redirect('manager_dashboard')
#    if request.method=="POST":
#        username=request.POST['username']
#        password=request.POST['password']
#        if not len(username):
#            messages.warning(request, "Username field is empty")
#            redirect('user_login')
#        elif not len(password):
#            messages.warning(request, "Password field is empty")
#            redirect('user_login')
#        else:
#            pass
#        if Customer.objects.filter(username=username):
#            user=Customer.objects.filter(username=username)[0]
#            password_hash=user.password
#            res=check_password(password, password_hash)
#            if res==1:
#                request.session['username'] = username
#                request.session['type'] = 'customer'
#                return render(request, 'booking/index.html', {})
#            else:
#                messages.warning(request, "Username or password is incorrect")
#                redirect('user_login')
#        else:
#            messages.warning(request, "No Account exists for the given Username")
#            redirect('user_login')
#    else:
#        redirect('user_login')
#    return render(request, 'login/user_login.html', {})
    

#def manager_login(request):
#    if request.session.get('username', None) and request.session.get('type', None)=='customer':
#        return redirect('user_dashboard')
#    if request.session.get('username', None) and request.session.get('type', None)=='manager':
#        return redirect('manager_dashboard')
#    if request.method=="POST":
#        username=request.POST['username']
#        password=request.POST['password']
#        if not len(username):
#            messages.warning(request, "Username field is empty")
#            redirect('manager_login')
#        elif not len(password):
    #         messages.warning(request, "Password field is empty")
    #         redirect('manager_login')
    #     else:
    #         pass
    #     if Technician.objects.filter(username=username):
    #         user=Technician.objects.filter(username=username)[0]
    #         password_hash=user.password
    #         res=check_password(password, password_hash)
    #         if res==1:
    #             # Adds necessary approval to be able to log into a staff account
    #             if user.approved:
    #                 request.session['username'] = username
    #                 request.session['type'] = 'manager'
    #                 return render(request, 'booking/index.html', {})
    #             else:
    #                 messages.warning(request, "Your account is awaiting approval")
    #                 redirect('manager_login')
    #         else:
    #             messages.warning(request, "Username or password is incorrect")
    #             redirect('manager_login')
    #     else:
    #         messages.warning(request, "No account exists for the given Username")
    #         redirect('manager_login')
    # else:
    #     redirect('manager_login')
    # return render(request, 'login/manager_login.html', {})


# def user_signup(request):
#     if request.session.get('username', None) and request.session.get('type', None)=='customer':
#         return redirect('user_dashboard')
#     if request.session.get('username', None) and request.session.get('type', None)=='manager':
#         return redirect('manager_dashboard')
#     if request.method=="POST":
#         username=request.POST['username']
#         email=request.POST['email']
#         if Customer.objects.filter(username=username) or Customer.objects.filter(email=email):
#             messages.warning(request, "Account already exists,  please Login to continue")
#         else:
#             password=request.POST['password']
#             address=request.POST['address']
#             pin_code=request.POST['pin_code']
#             profile_pic=request.FILES.get('profile_pic', None)
#             phone_no=request.POST['phone_no']
#             state=request.POST['state']
#             error=[]
#             if(len(username)<3):
#                 error.append(1)
#                 messages.warning(request, "Username Field must be greater than 3 character.")
#             if(len(password)<5):
#                 error.append(1)
#                 messages.warning(request, "Password Field must be greater than 5 character.")
#             if(len(email)==0):
#                 error.append(1)
#                 messages.warning(request, "Email field can't be empty")
#             if(len(phone_no)!=10):
#                 error.append(1)
#                 messages.warning(request, "Valid Phone number is a 10 digit-integer.")
#             if(len(error)==0):
#                 password_hash = make_password(password)
#                 customer=Customer(username=username, password=password_hash, email=email, phone_no=phone_no, address=address, state=state, pin_code=pin_code, profile_pic=profile_pic)
#                 customer.save()
#                 messages.info(request, "Account Created Successfully,  please Login to continue")
#                 redirect('user_signup')
#             else:
#                 redirect('user_signup')
        
#     else:
#         redirect('user_signup')
#     return render(request, 'login/user_login.html', {})


# def manager_signup(request):
#     if request.session.get('username', None) and request.session.get('type', None)=='customer':
#         return redirect('user_dashboard')
#     if request.session.get('username', None) and request.session.get('type', None)=='manager':
#         return redirect('manager_dashboard')
#     if request.method=="POST":
#         username=request.POST['username']
#         email=request.POST['email']
#         if Technician().objects.filter(username=username) or Technician.objects.filter(email=email):
#            messages.warning(request, "Account already exist,  please Login to continue")
#         else:
#             password=request.POST['password']
#             profile_pic=request.FILES.get('profile_pic', None)
#             phone_no=request.POST['phone_no']
#             error=[]
#             if(len(username)<3):
#                 error.append(1)
#                 messages.warning(request, "Username Field must be greater than 3 character.")
#             if(len(password)<5):
#                 error.append(1)
#                 messages.warning(request, "Password Field must be greater than 5 character.")
#             if(len(email)==0):
#                 error.append(1)
#                 messages.warning(request, "Email field can't be empty")
#             if(len(phone_no)!=10):
#                 error.append(1)
#                 messages.warning(request, "Valid Phone number is a 10 digit-integer.")
#             if(len(error)==0):
#                 password_hash = make_password(password)
#                 r_manager=Technician(username=username, password=password_hash, email=email, phone_no=phone_no, profile_pic=profile_pic)
#                 r_manager.save()
#                 messages.info(request, "Account Created Successfully,  Please login to continue")
#                 redirect('manager_signup')
#             else:
#                 redirect('manager_signup')
        
#     else:
#         redirect('user_signup')
#     return render(request, 'login/manager_login.html', {})
# def logout(request):
#     if request.session.get('username',  None):
#         del request.session['username']
#         del request.session['type']
#         return render(request, "login/logout.html", {})
#     else:
#         return render(request, "login/user_login.html", {})

