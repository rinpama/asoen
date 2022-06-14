from django import forms
from .models import  GenreM,SoenMemberM,soenmemberDetailM,VehicleM,SpecialEducationM,HealthM ,InsuranceM,SkillM, LicenceM


class GenreF(forms.ModelForm):
    class Meta():
        model=GenreM
        fields = '__all__'


class SoenMemberF(forms.ModelForm):
    class Meta():
        model=SoenMemberM
        fields = '__all__'


class soenmemberDetailF(forms.ModelForm):
    class Meta():
        model=soenmemberDetailM
        # fields = '__all__'
        fields = ['add', 'tel', 'age', 'bloodtype']
class InsuranceF(forms.ModelForm):
    class Meta():
        model=InsuranceM
        fields = ['Insurance_station', 'healthInsurance', 'pensionInsurance', 'employmentinsurance']
class VehicleF(forms.ModelForm):
    class Meta():
        model=VehicleM
        fields = ['vehicleNumber', 'firstUse', 'finishUse', 'vehicleModel']

class HealthF(forms.ModelForm):
    class Meta():
        model=HealthM
        fields = ['consaltationDay', 'bloodPressureHigh', 'bloodPressureLow']

class SpecialEducationF(forms.ModelForm):
    class Meta():
        model=SpecialEducationM
        fields = ['specialeducation']

class SkillF(forms.ModelForm):
    class Meta():
        model=SkillM
        fields = ['skill_name']


class LicenceF(forms.ModelForm):
    class Meta():
        model=LicenceM
        fields = ['licence_name']