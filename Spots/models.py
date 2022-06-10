from django.db import models
from Soen.models import VehicleM
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

def check_age(value):
    if value<10 or value>100:
        raise ValidationError('10～100歳の登録でお願いします')
# Create your models here.
# CompanyGenreM,SpotCompanyM,spotcompanyDetailM

class CompanyGenreM(models.Model):
    companygenre = models.CharField(max_length=20, default='')
    def __str__(self):
        # return self.genre +'(id='+ str(self.id) +')'
        return self.companygenre
    class Meta:
        verbose_name_plural = "会社ジャンル"

class SpotCompanyM(models.Model):
    genre = models.ForeignKey(CompanyGenreM, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=40,validators=[MinLengthValidator(2,'2文字以上としてください')])
    def __str__(self):
        return self.name + '( ID => ' + str(self.id) + ')'
    class Meta:
        verbose_name_plural = "Spot & Company"

class spotcompanyDetailM(models.Model):
    man = models.OneToOneField(SpotCompanyM, on_delete=models.CASCADE, related_name='spotcompanyD', default='')
    tel = models.CharField('電話番号', max_length=15, default='', blank=True, null=True,validators=[RegexValidator(r'^[a-zA-Z0-9]*$','英数字のみ入力可')])
    fax = models.CharField('FAX番号', max_length=10, default='', blank=True, null=True,validators=[RegexValidator(r'^[a-zA-Z0-9]*$','英数字のみ入力可')])
    add = models.CharField('住所', max_length=100, default='', blank=True, null=True,)
    vehicle=models.ManyToManyField('Soen.VehicleM', blank=True, null=True,)
    def __str__(self):
        return str(self.man) + '(' + str(self.add) + ')'
    class Meta:
        verbose_name_plural = "SpotCompany詳細"