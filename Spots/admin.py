from django.contrib import admin

# Register your models here.
# CompanyGenreM,SpotM,CompanyM
from .models import CompanyGenreM,SpotGenreM,SpotM,CompanyM,SpotDetailM,CompanyDetailM

admin.site.register(CompanyGenreM)
admin.site.register(SpotGenreM)
admin.site.register(SpotM)
admin.site.register(CompanyM)
admin.site.register(SpotDetailM)
admin.site.register(CompanyDetailM)