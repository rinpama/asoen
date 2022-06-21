from django.contrib import admin

# Register your models here.
# CompanyGenreM,SpotM,CompanyM
from .models import CompanyGenreM,SpotM,CompanyM

admin.site.register(CompanyGenreM)
admin.site.register(SpotM)
admin.site.register(CompanyM)