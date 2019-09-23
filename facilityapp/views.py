from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from . import models
import os 


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

class FacilityCreate(CreateView):
    template_name = os.path.join('facilityapp', 'facility-create.html')
    form_class = FacilityForm

class FacilityDetail(DetailView):
    model = models.Facility
    template_name = os.path.join('detail','facility-detail.html')

class FacilityList(ListView):
    template_name = os.path.join('list','facility-list.html')
    context_object_name = 'facility'

    def get_queryset(self):
        return models.Facility.objects.order_by('pk')

class FacilityUpdate(UpdateView):
    form_class = FacilityForm
    model = models.Facility
    template_name = os.path.join('facilityapp','facility-create.html')

class FacilityDelete(DeleteView):
    model = models.Facility
    template_name = os.path.join('facilityapp','facility_confirm_delete.html')
    success_url = reverse_lazy('facilityapp:facility-list')