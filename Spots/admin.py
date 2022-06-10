from django.contrib import admin

# Register your models here.
from .models import CompanyGenreM,SpotCompanyM,spotcompanyDetailM

admin.site.register(CompanyGenreM)
admin.site.register(SpotCompanyM)
admin.site.register(spotcompanyDetailM)