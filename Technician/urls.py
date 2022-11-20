from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name="manager_dashboard"),
    path('new/',views.add_technician,name="add_technician"),
    path('update/<int:technician_no>/',views.update_technician,name="update_technician"),
]