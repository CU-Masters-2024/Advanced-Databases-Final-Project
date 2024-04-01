from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from .models import Patient, Physician, Treatment, MedicalProfile
# Create your views here.


class HomeView(CreateView):
    model = Patient
    fields = '__all__'
    template_name = 'home.html'
    success_url = '/success/'

    # def get(self, request):
    #     form = Patient
    #     return render(request, self.template_name, context={'form' : form} ) 

    # def post(self, request):
    #     form = Patient(request.POST)
    #     if form.is_valid():
    #         print(form)


class PhysicianView(CreateView):
    model  = Physician
    fields = '__all__'
    template_name = 'physician.html'
    success_url = '/success/'


class MedicalProfileView(CreateView):
    model  = MedicalProfile
    fields = '__all__'
    template_name = 'medical-profile.html'
    success_url = '/success/'


class TreatmentView(CreateView):
    model  = Treatment
    fields = '__all__'
    template_name = 'treatment.html'
    success_url = '/success/'

    
class SuccessView(TemplateView):
    template_name = "success.html"
    

class SampleData(TemplateView):
    template_name = 'sample_data.html'
