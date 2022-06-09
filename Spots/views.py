from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SpotsTop(TemplateView):
    template_name='Spots/spotstop.html'

class SpotCreate(CreateView):
    pass