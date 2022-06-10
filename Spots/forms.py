from django import forms
from .models import CompanyGenreM,SpotCompanyM,spotcompanyDetailM
#CompanyGenreF,SpotCompanyF,spotcompanyDetailF


class CompanyGenreF(forms.ModelForm):
    class Meta():
        model=CompanyGenreM
        fields = '__all__'

class SpotCompanyF(forms.ModelForm):
    class Meta():
        model=SpotCompanyM
        fields = '__all__'

class spotcompanyDetailF(forms.ModelForm):
    class Meta():
        model=spotcompanyDetailM
        fields = '__all__'