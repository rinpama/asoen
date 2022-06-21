from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import CompanyGenreM,SpotM,CompanyM
from .forms import CompanyGenreF,SpotF,CompanyF
# Create your views here.



# *********************************** login before-after ***********************************************
class SpotsTop(TemplateView):
    template_name='Spots/spotstop.html'

######################################################################
class SpotCreate(CreateView):
    model = SpotM
    form_class = SpotF
    template_name = 'Spots/spotcreate.html'

    def get_success_url(self):
        return reverse('Spots:spotstop')