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
        fields = '__all__'



class VehicleF(forms.ModelForm):
    class Meta():
        model=VehicleM
        fields = '__all__'


class SpecialEducationF(forms.ModelForm):
    class Meta():
        model=SpecialEducationM
        fields = '__all__'


class HealthF(forms.ModelForm):
    class Meta():
        model=HealthM
        fields = '__all__'


class SkillF(forms.ModelForm):
    class Meta():
        model=SkillM
        fields = '__all__'


class LicenceF(forms.ModelForm):
    class Meta():
        model=LicenceM
        fields = '__all__'