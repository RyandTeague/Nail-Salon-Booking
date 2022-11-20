from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('book',views.book,name='book'),
    path('contact-us',views.contact,name='contact-us'),
    path('book-now/<str:id>',views.book_now,name='book-now'),
    path('cancel-treatment/<str:id>',views.cancel_treatment,name='cancel-treatment'),
    path('delete-treatment/<str:id>',views.delete_treatment,name='delete-treatment'),
    # path('confirm-now-booking',views.book_confirm,name="book_confirm"),

]