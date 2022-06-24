from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import CompanyGenreM, SpotM, CompanyM,CompanyDetailM,SpotDetailM
from .forms import CompanyGenreF, SpotF, CompanyF, SpotDetailF,CompanyDetailF, IdSearchF


# Create your views here.

###########################各種　簡易を元にDetailをCreate##################
@login_required
def CreateDetailCompany(request,number):
    name=CompanyM.objects.get(pk=number)
    params={
        'name':name.name,
        'form':CompanyDetailF(),
    }
    if(request.method=='POST'):
        data=CompanyDetailM(companydetail_id=name.pk)
        record=CompanyDetailF(request.POST,instance=data)
        record.save()
        return redirect(to='account:logintop')
    return render(request,'Spots/createdetailcompany.html',params)

@login_required
def CreateDetailAspot(request,number):
    name=SpotM.objects.get(pk=number)
    params={
        'name':name.spotname,
        'form':SpotDetailF(),
    }
    if(request.method=='POST'):
        data=SpotDetailM(spotdetail_id=name.id)
        record=SpotDetailF(request.POST,instance=data)
        record.save()
        return redirect(to='account:logintop')
    return render(request,'Spots/createdetailcompany.html',params)

###########################各種　LIST##################
@login_required
def logSoenList(request):
    data=CompanyM.objects.filter(genre_id=2)
    params={
        'data':data,
    }
    return render(request,'Spots/logcompanylist.html',params)
@login_required
def logGeneList(request):
    data = CompanyM.objects.filter(genre_id=5)
    params = {
        'data': data,
    }
    return render(request, 'Spots/logcompanylist.html', params)
@login_required
def logKyouryokuList(request):
    data = CompanyM.objects.filter(Q(genre_id=3)|Q(genre_id=4))
    params = {
        'data': data,
    }
    return render(request, 'Spots/logcompanylist.html', params)

@login_required
def logAspotList(request):
    data = SpotM.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'Spots/logaspotlist.html', params)
###########################各種　Detail表示##################
@login_required
def LogCompanyDetail(request,number):
    data = CompanyM.objects.get(pk=number)
    params = {
        'data': data,
    }
    return render(request, 'Spots/logcompanydetail.html', params)
@login_required
def LogAspotDetail(request,number):
    data = SpotM.objects.get(pk=number)
    params = {
        'data': data,
    }
    return render(request, 'Spots/logaspotdetail.html', params)

# *********************************** login before-after ***********************************************
###########################Spot Top画面表示##################
class SpotsTop(TemplateView):
    template_name = 'Spots/spotstop.html'

###########################各種　LIST表示（検索付）##################
def spotlist(request):
    params = {
        'data': [],  # SpotM.objects.all()
    }
    if (request.method == 'POST'):
        word = request.POST['words']
        serchedData = SpotM.objects.filter(Q(name__icontains=word))
        params = {
            'serchedData': serchedData,
            'form': IdSearchF(request.POST),
            'listname': '検索した現場LIST',
        }
    else:
        params = {
            'data': SpotM.objects.all(),
            'form': IdSearchF(),
            'listname': '現場LIST',
        }
    return render(request, 'Spots/spotCompanylist.html', params)

def generallist(request):
    params = {
        'data': [],
    }
    if (request.method == 'POST'):
        word = request.POST['words']
        serchedData = CompanyM.objects.filter(Q(name__icontains=word))
        params = {
            'serchedData': serchedData,
            'form': IdSearchF(request.POSt),
            'listname': '検索した上位/元請LIST'
        }
    else:
        params = {
            'data': CompanyM.objects.filter(Q(genre='5')),
            'form': IdSearchF(),
            'listname': '上位/元請LIST',
        }
    return render(request, 'Spots/spotCompanylist.html', params)

def cooperatelist(request):
    params = {
        'data': [],
    }
    if (request.method == 'POST'):
        word = request.POST['words']
        serchedData = CompanyM.objects.filter((Q(genre='4') | Q(genre='3')),Q(name__icontains=word))
        params = {
            'serchedData': serchedData,
            'form': IdSearchF(request.POST),
            'listname': '検索した協力会社A/B LIST',
        }
    else:
        params = {
            'data': CompanyM.objects.filter(Q(genre='4') | Q(genre='3')),
            'form': IdSearchF(),
            'listname': '協力会社A/B LIST',
        }
    return render(request, 'Spots/spotCompanylist.html', params)

def soenlist(request):
    data = CompanyM.objects.filter(genre=2)
    params = {
        'data': data,
        'listname': '装苑DATA'
    }
    return render(request, 'Spots/spotCompanylist.html', params)

###########################各種　簡易Create##################
class SpotCreate(CreateView):
    model = SpotM
    form_class = SpotF
    template_name = 'Spots/spotCompanycreate.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = '工事現場 新規作成'
        return context
    def get_success_url(self):
        return reverse('Spots:spotstop')

class CompanyCreate(CreateView):
    model = CompanyM
    form_class = CompanyF
    template_name = 'Spots/spotCompanycreate.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = '各会社 新規作成'
        return context
    def get_success_url(self):
        return reverse('Spots:spotstop')

###########################各種　簡易＆Detail　Create##################
def CreateSpotDetail(request):
    params = {
        'form': SpotF(),
        'form2': SpotDetailF(),
    }
    if (request.method == 'POST'):
        record1 = SpotF(request.POST)
        record2 = SpotDetailF(request.POST)
        if all((record1.is_valid(), record2.is_valid())):
            member = record1.save(commit=False)
            member.save()
            detail = record2.save(commit=False)
            detail.spotDetail = member
            detail.save()
            return redirect(to='accounts:logintop')
    return render(request, 'Soen/logcreate/createdetailmember.html', params)

def CreateCompanyDetail(request):
    params = {
        'form': CompanyF(),
        'form2': CompanyDetailF(),
    }
    if (request.method == 'POST'):
        record1 = CompanyF(request.POST)
        record2 = CompanyDetailF(request.POST)
        if all((record1.is_valid(), record2.is_valid())):
            member = record1.save(commit=False)
            member.save()
            detail = record2.save(commit=False)
            detail.companyDetail = member
            detail.save()
            return redirect(to='accounts:logintop')
    return render(request, 'Soen/logcreate/createdetailmember.html', params)