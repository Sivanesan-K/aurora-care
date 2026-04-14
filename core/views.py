from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Caretaker, Doctor, Booking, SkinAnalysis

def home(request):
    return render(request, 'home.html')

def caretakers(request):
    data = Caretaker.objects.all()
    return render(request, 'caretakers.html', {'caretakers': data})

def doctors(request):
    data = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': data})

def skin(request):
    result = None
    if request.method == 'POST':
        image = request.FILES.get('image')
        result = "Possible mild rash detected. Please keep the area clean and use antiseptic cream. Consult a doctor if it worsens."
    return render(request, 'skin.html', {'result': result})

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already taken!'})
        User.objects.create_user(username=username, password=password)
        return redirect('/login/')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'error': 'Wrong username or password!'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def book_caretaker(request, pk):
    caretaker = get_object_or_404(Caretaker, id=pk)
    if request.method == 'POST':
        date = request.POST.get('date')
        message = request.POST.get('message')
        Booking.objects.create(user=request.user, caretaker=caretaker, date=date, message=message)
        return redirect('/booking-success/')
    return render(request, 'book.html', {'person': caretaker, 'type': 'Caregiver'})

@login_required(login_url='/login/')
def book_doctor(request, pk):
    doctor = get_object_or_404(Doctor, id=pk)
    if request.method == 'POST':
        date = request.POST.get('date')
        message = request.POST.get('message')
        Booking.objects.create(user=request.user, doctor=doctor, date=date, message=message)
        return redirect('/booking-success/')
    return render(request, 'book.html', {'person': doctor, 'type': 'Doctor'})

@login_required(login_url='/login/')
def booking_success(request):
    return render(request, 'booking_success.html')

@login_required(login_url='/login/')
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})