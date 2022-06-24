from django import forms
from .models import CompanyGenreM,SpotM,SpotDetailM,CompanyM,CompanyDetailM
#CompanyGenreF,SpotCompanyF,spotcompanyDetailF,IdSearchF

class IdSearchF(forms.Form):
    words = forms.CharField(label='Word検索', max_length=15)

class CompanyGenreF(forms.ModelForm):
    class Meta():
        model=CompanyGenreM
        fields = ['companygenre',]

class SpotF(forms.ModelForm):
    class Meta():
        model=SpotM
        fields = ['genre','spotname',]

class SpotDetailF(forms.ModelForm):
    class Meta():
        model=SpotDetailM
        fields = ['locationmanager']

class CompanyF(forms.ModelForm):
    class Meta():
        model=CompanyM
        fields = ['genre','name','add']

class CompanyDetailF(forms.ModelForm):
    class Meta():
        model=CompanyDetailM
        fields = ['president']