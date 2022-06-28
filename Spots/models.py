from django.db import models
from Soen.models import SoenMemberM,VehicleM
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

def check_age(value):
    if value<10 or value>100:
        raise ValidationError('10～100歳の登録でお願いします')
# Create your models here.
# CompanyGenreM,SpotGenreM,SpotM,CompanyM,SpotDetailM,CompanyDetailM

class CompanyGenreM(models.Model):
    companygenre = models.CharField(max_length=20, unique=True,default='')
    def __str__(self):
        return self.companygenre +'(id='+ str(self.id) +')'
        # return self.companygenre
    class Meta:
        verbose_name_plural = "Companyジャンル"

class CompanyM(models.Model):
    genre = models.ForeignKey(CompanyGenreM, on_delete=models.CASCADE,)
    name = models.CharField(max_length=40, validators=[MinLengthValidator(2, '2文字以上としてください')])
    add = models.CharField('住所', max_length=100, default='', blank=True, null=True, )
    tel = models.CharField('電話番号', max_length=15, default='', blank=True, null=True,validators=[RegexValidator(r'^[a-zA-Z0-9-]*$','英数字のみ入力可')])
    fax = models.CharField('FAX番号', max_length=10, default='', blank=True, null=True,validators=[RegexValidator(r'^[a-zA-Z0-9-]*$','英数字のみ入力可')])

    vehicle=models.ManyToManyField('Soen.VehicleM', default='', blank=True, null=True,)
    def __str__(self):
        return str(self.name) + '(' + str(self.add) + ')'
    class Meta:
        verbose_name_plural = "各 会社"

class CompanyDetailM(models.Model):
    companydetail=models.OneToOneField(CompanyM,on_delete=models.CASCADE,related_name='companyDetail')
    president=models.CharField(max_length=30, default='', blank=True, null=True,)#社長
    def __str__(self):
        return str(self.companydetail) + '(' + str(self.president) + ')'
    class Meta:
        verbose_name_plural = "各 会社詳細"

class SpotGenreM(models.Model):
    spotgenre = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.spotgenre +'(id='+ str(self.id) +')'
        # return self.companygenre
    class Meta:
        verbose_name_plural = "spotジャンル"

class SpotM(models.Model):
    genre = models.ForeignKey(SpotGenreM, on_delete=models.CASCADE)
    spotname = models.CharField(max_length=40,validators=[MinLengthValidator(2,'2文字以上としてください')])
    add = models.CharField('住所', max_length=100, default='', blank=True, null=True, )
    tel = models.CharField('電話番号', max_length=15, default='', blank=True, null=True,
                           validators=[RegexValidator(r'^[a-zA-Z0-9-]*$', '英数字のみ入力可')])
    fax = models.CharField('FAX番号', max_length=10, default='', blank=True, null=True,
                           validators=[RegexValidator(r'^[a-zA-Z0-9-]*$', '英数字のみ入力可')])
    generalCompany = models.ForeignKey(CompanyM,on_delete=models.CASCADE, blank=True, null=True)
    primaryCompany=models.ForeignKey(CompanyM,related_name='primarycompany',on_delete=models.CASCADE, blank=True, null=True)
    primaryCompanyMember=models.ManyToManyField(SoenMemberM)
    secondaryCompany=models.ForeignKey(CompanyM,related_name='secondarycompany',on_delete=models.CASCADE, blank=True, null=True)
    thirdCompany=models.ForeignKey(CompanyM,related_name='thirdcompany',on_delete=models.CASCADE, blank=True, null=True)
    forthCompany=models.ForeignKey(CompanyM,related_name='forthcompany',on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '現場: '+str(self.spotname) +' ///1次: '+str(self.primaryCompany) +' ///2次: '+str(self.secondaryCompany)+' ///3次: '+str(self.thirdCompany)+' ///4次: '+str(self.forthCompany)+' ///1次ﾒﾝﾊﾞｰ: '+str(self.primaryCompanyMember.all())
    class Meta:
        verbose_name_plural = "工事現場"

class SpotDetailM(models.Model):
    spotdetail=models.OneToOneField(SpotM,on_delete=models.CASCADE,related_name='spotDetail')
    locationmanager=models.CharField(max_length=30)#現場所長
    def __str__(self):
        return str(self.spotdetail)+'-----'+str(self.locationmanager)
    class Meta:
        verbose_name_plural = "工事現場詳細"