from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('caretakers/', views.caretakers),
    path('doctors/', views.doctors),
    path('skin/', views.skin),
    path('register/', views.register_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('book-caretaker/<int:pk>/', views.book_caretaker),
    path('book-doctor/<int:pk>/', views.book_doctor),
    path('booking-success/', views.booking_success),
    path('my-bookings/', views.my_bookings),
]