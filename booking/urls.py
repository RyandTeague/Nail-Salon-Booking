from django.urls import path
from . import views


urlpatterns=[
    #path('',views.index,name='index'),
    #path('book',views.book,name='book'),
    path('contact-us',views.contact,name='contact-us'),
    #path('book-now/<str:id>',views.book_now,name='book-now'),
    #path('cancel-treatment/<str:id>',views.cancel_treatment,name='cancel-treatment'),
    #path('delete-treatment/<str:id>',views.delete_treatment,name='delete-treatment'),
    # path('confirm-now-booking',views.book_confirm,name="book_confirm"),
    path('', views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<int:id>', views.userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel', views.staffPanel, name='staffPanel'),
]