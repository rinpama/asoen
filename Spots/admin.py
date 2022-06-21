from django.contrib import admin

# Register your models here.
# CompanyGenreM,SpotM,CompanyM
from .models import CompanyGenreM,SpotGenreM,SpotM,CompanyM

admin.site.register(CompanyGenreM)
admin.site.register(SpotGenreM)
admin.site.register(SpotM)
admin.site.register(CompanyM)