from django.urls import path,include
from . import views
urlpatterns=[
    #login/logout/register
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register'),
#    path('login',views.user_login,name='user_login'),
#    path('login1',views.manager_login,name='manager_login'),
#    path('signup',views.user_signup,name='user_signup'),
#    path('signup1',views.manager_signup,name='manager_signup'),
#    path('dashboard/',include('customer.urls')),
#    path('dashboard1/',include('Technician.urls')),
#    path('add-treatment/',include('Technician.urls'))
]