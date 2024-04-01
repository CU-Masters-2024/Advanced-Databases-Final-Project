from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Patient)
admin.site.register(Physician)
admin.site.register(Treatment)
admin.site.register(MedicalProfile)