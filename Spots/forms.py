from django import forms
from .models import CompanyGenreM,SpotM,CompanyM
#CompanyGenreF,SpotCompanyF,spotcompanyDetailF


class CompanyGenreF(forms.ModelForm):
    class Meta():
        model=CompanyGenreM
        fields = '__all__'

class SpotF(forms.ModelForm):
    class Meta():
        model=SpotM
        fields = '__all__'

class CompanyF(forms.ModelForm):
    class Meta():
        model=CompanyM
        fields = '__all__'