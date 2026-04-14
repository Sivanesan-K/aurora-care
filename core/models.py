from django.db import models
from django.contrib.auth.models import User

class Caretaker(models.Model):
    name = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caretaker = models.ForeignKey(Caretaker, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}"

class SkinAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='skin/')
    result = models.TextField()

    def __str__(self):
        return f"{self.user.username}"