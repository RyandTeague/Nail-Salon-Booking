"""nailsalon2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import views as users_views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/treatments/<uuid:treatment_id>/checkin',views.treatment_checkin, name = 'treatment_checkin'),
    # path('/treatments/<uuid:treatment_id>/checkout',views.treatment_checkout, name = 'treatment_checkout'),
    path('treatments/', views.treatments, name='treatments'),
    path('treatments/<uuid:treatment_id>/', views.treatments_detailed_view, name='treatments_detailed_view'),
    path('treatments/<uuid:treatment_id>/booking/', views.booking, name='booking'),
    path('', views.homepage, name='salon-home'),
    path('about/', views.about, name='salon-about'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('admin', views.admin_list, name='admin-list'),
    path('admin/create', users_views.admin_create, name='register'),
    path('profile/', users_views.profile, name='profile'),
    path('/admin/create', views.admin_create, name='admin-create'),
    path('/admin/<uuid:staff_id>', views.show_admin, name= 'admin-staff'),
    path('/admin/<uuid:staff_id>/edit', views.edit_admin, name= 'admin-staff-edit'),
    path('/admin/<uuid:staff_id>/delete', views.delete_admin, name='admin-staff-delete'),
    path('login', auth_views.LoginView.as_view(template_name = 'salon/login.html'), name= 'admin-login'),
    path('logout', auth_views.LogoutView.as_view(template_name= 'salon/logout.html'), name= 'admin-logout'),
    path('/admin/logs',views.logs, name = 'logs')
]
