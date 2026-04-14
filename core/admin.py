from django.contrib import admin
from .models import Caretaker, Doctor, Booking, SkinAnalysis

admin.site.register(Caretaker)
admin.site.register(Doctor)
admin.site.register(Booking)
admin.site.register(SkinAnalysis)