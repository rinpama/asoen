from django import forms
from .models import CompanyGenreM,SpotM,CompanyM
#CompanyGenreF,SpotCompanyF,spotcompanyDetailF


class CompanyGenreF(forms.ModelForm):
    class Meta():
        model=CompanyGenreM
        fields = ['companygenre',]

class SpotF(forms.ModelForm):
    class Meta():
        model=SpotM
        fields = ['genre','name',]

class SpotDetailF(forms.ModelForm):
    class Meta():
        model=SpotM
        fields = '__all__'

class CompanyF(forms.ModelForm):
    class Meta():
        model=CompanyM
        fields = ['genre','name','add','tel','fax']