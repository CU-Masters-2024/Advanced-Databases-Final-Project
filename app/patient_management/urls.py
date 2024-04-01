from django.urls import path 

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('patient/', HomeView.as_view(), name="patient"),
    path('physician/', PhysicianView.as_view(), name="physician"),
    path('medical-profile/', MedicalProfileView.as_view(), name="medical-profile"),
    path('treatment/', TreatmentView.as_view(), name="treatment"),
    path('sample-data', SampleData.as_view(), name='sample-data'),
    path('success/', SuccessView.as_view(), name="success"),
]
