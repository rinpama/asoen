from django.contrib import admin

# Register your models here.
from .models import GenreM,SoenMemberM,soenmemberDetailM,VehicleM,SpecialEducationM,HealthM ,InsuranceM,SkillM, LicenceM
# GenreM,SoenMemberM,soenmemberDetailM,VehicleM,SpecialEducationM,HealthM ,InsuranceM,SkillM, LicenceM

admin.site.register(LicenceM)
admin.site.register(SkillM)
admin.site.register(InsuranceM)
admin.site.register(HealthM)
admin.site.register(SpecialEducationM)
admin.site.register(VehicleM)
admin.site.register(soenmemberDetailM)
admin.site.register(SoenMemberM)
admin.site.register(GenreM)