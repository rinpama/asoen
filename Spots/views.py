from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import CompanyGenreM,SpotM,CompanyM
from .forms import CompanyGenreF,SpotF,CompanyF,SpotDetailF
# Create your views here.



# *********************************** login before-after ***********************************************
class SpotsTop(TemplateView):
    template_name='Spots/spotstop.html'

def spotlist(request):
    data=SpotM.objects.all()
    params={
        'data':data,
        'listname':'現場LIST'
    }
    return render(request, 'Spots/spotCompanylist.html', params)
def generallist(request):
    data = CompanyM.objects.filter(genre=5)
    params = {
        'data': data,
        'listname': '上位/元請LIST'
    }
    return render(request, 'Spots/spotCompanylist.html', params)
def cooperatelist(request):
    data = CompanyM.objects.filter(Q(genre='4') | Q(genre='3'))
    params = {
        'data': data,
        'listname': '協力会社A/B LIST'
    }
    return render(request, 'Spots/spotCompanylist.html', params)
def soenlist(request):
    data = CompanyM.objects.filter(genre=2)
    params = {
        'data': data,
        'listname': '装苑DATA'
    }
    return render(request, 'Spots/spotCompanylist.html', params)
######################################################################
class SpotCreate(CreateView):
    model = SpotM
    form_class = SpotDetailF
    template_name = 'Spots/spotCompanycreate.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['message'] = 'お手数ですが、Genre「工事現場」を指定してください。'
    #     return context
    def get_success_url(self):
        return reverse('Spots:spotstop')
class CompanyCreate(CreateView):
    model = SpotM
    form_class = CompanyF
    template_name = 'Spots/spotCompanycreate.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['message'] = 'お手数ですが、Genre「工事現場 以外のもの」をを指定してください。'
    #     return context
    def get_success_url(self):
        return reverse('Spots:spotstop')