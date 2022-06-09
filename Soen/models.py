from django.db import models

from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

def check_age(value):
    if value<10 or value>100:
        raise ValidationError('10～100歳の登録でお願いします')
# Create your models here.
# GenreM,SoenMemberM,soenmemberDetailM,VehicleM,HealthM InsuranceM,SpecialEducationM,SkillM, LicenceM

class GenreM(models.Model):
    genre = models.CharField(max_length=20, default='')
    def __str__(self):
        # return self.genre +'(id='+ str(self.id) +')'
        return self.genre
    class Meta:
        verbose_name_plural = "業者ジャンル"

class SoenMemberM(models.Model):
    genre = models.ForeignKey(GenreM, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=40,validators=[MinLengthValidator(2,'2文字以上としてください')])
    def __str__(self):
        return self.name + '( ID => ' + str(self.id) + ')'
    class Meta:
        verbose_name_plural = "SoenMember"

class soenmemberDetailM(models.Model):
    man = models.OneToOneField(SoenMemberM, on_delete=models.CASCADE, related_name='soenmemberD', default='')
    # update = models.DateTimeField('更新日', auto_now_add=True)
    add = models.CharField('住所', max_length=60, default='長崎県佐世保市', blank=True, null=True)
    tel = models.CharField('電話番号', max_length=15, default='0956-', blank=True, null=True)
    bloodtype = models.CharField('血液型', max_length=10, default='ABOAB', blank=True, null=True)
    age = models.IntegerField('年齢', default='100', blank=True, null=True,validators=[RegexValidator(r'^[a-zA-Z0-9]*$','英数字のみ入力可')])
    def __str__(self):
        return str(self.man) + '(' + str(self.bloodtype) + ')'# + '<<更新' + str(self.update) + '>>'
    class Meta:
        verbose_name_plural = "SoenMember詳細"

class VehicleM(models.Model):
    man = models.ManyToManyField(SoenMemberM, related_name='soenmemberVehicle', default='')
    vehicleNumber = models.CharField(verbose_name="車両番号", max_length=20, default='佐世保　あ　50　50-50')
    firstUse = models.DateField(verbose_name="使用期間開始", null=True, blank=True)
    finishUse = models.DateField(verbose_name="使用期間終了", null=True, blank=True)
    vehicleModel = models.CharField(verbose_name="車検証_型式", max_length=20, null=True, blank=True)
    firstInspection = models.DateField(verbose_name="車検証_車検期間開始", null=True, blank=True)
    finishInspection = models.DateField(verbose_name="車検証_車検期間終了", null=True, blank=True)
    file1 = models.FileField(verbose_name="Link1車検証", max_length=100, null=True, blank=True)
    liabilityComp = models.CharField(verbose_name="自賠責_保険会社", max_length=20, null=True, blank=True)
    liability_num = models.CharField(verbose_name="自賠責_証券番号", max_length=20, null=True, blank=True)
    firstliability = models.DateField(verbose_name="自賠責_保険期間開始", null=True, blank=True)
    finishliability = models.DateField(verbose_name="自賠責_保険期間終了", null=True, blank=True)
    file2 = models.FileField(verbose_name="Link2自賠責", max_length=100, null=True, blank=True)
    voluntaryInsureComp = models.CharField(verbose_name="任意保険_保険会社", max_length=20, null=True, blank=True)
    voluntaryInsureNum = models.CharField(verbose_name="任意保険_証券番号", max_length=20, null=True, blank=True)
    firstVoluntary = models.DateField(verbose_name="任意保険_保険期間開始", null=True, blank=True)
    finishVoluntary = models.DateField(verbose_name="任意保険_保険期間終了", null=True, blank=True)
    voluntary_object = models.CharField(verbose_name="任意保険_対物_千円", max_length=20, null=True, blank=True)
    voluntary_human = models.CharField(verbose_name="任意保険_対人_千円", max_length=20, null=True, blank=True)
    voluntary_passenger = models.CharField(verbose_name="任意保険_搭乗者_千円", max_length=20, null=True, blank=True)
    file3 = models.FileField(verbose_name="Link3任意保険", max_length=100, null=True, blank=True)
    # driver = models.ManyToManyField('reimex.SoenModel')
    drive_departure = models.CharField(verbose_name="運転_出発地", max_length=100, null=True, blank=True)
    drive_waypoint1 = models.CharField(verbose_name="運転_経由1", max_length=100, null=True, blank=True)
    drive_waypoint2 = models.CharField(verbose_name="運転_経由2", max_length=100, null=True, blank=True)
    drive_arrival = models.CharField(verbose_name="運転_到着地", max_length=100, null=True, blank=True)
    def __str__(self):
        return self.vehicleNumber
    class Meta:
        verbose_name_plural = "車両"


class HealthM(models.Model):
    man = models.OneToOneField(SoenMemberM, on_delete=models.CASCADE, related_name='soenmemberHealth',default='')
    consaltationDay = models.DateField(verbose_name="診察日", null=True, blank=True)
    bloodPressureHigh = models.IntegerField(verbose_name='血圧(高)', null=True, blank=True)
    bloodPressureLow = models.IntegerField(verbose_name='血圧(低)', null=True, blank=True)
    def __str__(self):
        return str(self.consaltationDay)
    class Meta:
        verbose_name_plural = "健康診断"


class InsuranceM(models.Model):
    healthInsurance_list = [
        ('1', '健康保険組合'),
        ('2', '協会けんぽ（全国健康保険協会）'),
        ('3', '各種共済組合'),
        ('4', '国民健康保険'),
        ('5', '国民健康保険組合（長けん国保）'),
        ('6', '後期高齢者医療制度'),
        ('7', '船員保険（全国健康保険協会）'),
        ('8', '-')
    ]

    pensionInsurance_list = [
        ('1', '国民年金'),
        ('2', '厚生年金'),
        ('3', '-'),
    ]
    employmentinsurance_list = [
        ('1', '無'),
        ('2', '有'),
        ('3', '適用除外'),
        ('4', '-'),
    ]
    free_list = [
        ('1', '無'),
        ('2', '有'),
        ('3', '-'),
    ]
    man = models.OneToOneField(SoenMemberM, on_delete=models.CASCADE, related_name='soenmemberInsurance', default='')
    Insurance_station = models.CharField(verbose_name="保険＿事業所名", max_length=100, null=True, blank=True)
    Insurance_station_number = models.CharField(verbose_name="保険＿事業所名_整理記号･番号", max_length=100, null=True, blank=True)
    healthInsurance = models.CharField(verbose_name="健康保険", max_length=100, null=True, blank=True,
                                       choices=healthInsurance_list)
    file1 = models.FileField(verbose_name="Link1", max_length=100, null=True, blank=True)
    pensionInsurance = models.CharField(verbose_name="年金保険", max_length=100, null=True, blank=True,
                                        choices=pensionInsurance_list)
    file2 = models.FileField(verbose_name="Link2", max_length=100, null=True, blank=True)
    employmentinsurance = models.CharField(verbose_name="雇用保険", max_length=100, null=True, blank=True,
                                           choices=employmentinsurance_list)
    employmentinsurance_number = models.CharField(verbose_name="雇用保険番号", max_length=100, null=True, blank=True)
    file3 = models.FileField(verbose_name="Link3", max_length=100, null=True, blank=True)
    retirementCooperation = models.CharField(verbose_name="建退協", max_length=100, null=True, blank=True,
                                             choices=free_list)
    file4 = models.FileField(verbose_name="Link4", max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.Insurance_station)
    class Meta:
        verbose_name_plural = "社会保険"

# soenmodel特別教育_選択
class SpecialEducationM(models.Model):
    man = models.OneToOneField(SoenMemberM, on_delete=models.PROTECT, related_name='soenmemberEducation',default='')
    specialeducation_list = [
        ('0', '-'),
        ('研と', '研削といし取替・試運転'),
        ('ｱｰｸ', 'アーク溶接作業'),
        ('ﾌｫｰｸ', 'フォークリフト運転業務'),
        ('高作車', '高所作業車の運転'),
        ('巻機', '巻き上げ機の運転'),
        ('ｸﾚｰﾝ', 'クレーンの運転'),
        ('移ｸﾚｰﾝ', '移動式クレーンの運転'),
        ('玉掛', '玉掛け業務'),
        ('職', '職長教育'),
        ('職(追)', '職長教育（追教育）'),

        ('安衛責', '安全衛生責任者'),
        ('足場', '足場組立等作業従事者特別教育'),
        ('有溶剤', '有機溶剤取扱い業務'),
        ('特14', '特別教育14'),
        ('特15', '特別教育15'),
    ]
    specialeducation = models.CharField(verbose_name="特別教育", max_length=30, null=True, blank=True,
                                        choices=specialeducation_list)
    def __str__(self):
        return str(self.specialeducation)
    class Meta:
        verbose_name_plural = "特別教育"


class SkillM(models.Model):
    skillTraning_list = [
        ('-', '-'),
        ('有機溶剤作業主任者', '有機溶剤作業主任者'),
        ('玉掛け技能講習', '玉掛け技能講習'),
        ('特定化学物質等作業主任者', '特定化学物質等作業主任者'),
        ('小型移動式クレン運転技能講習', '小型移動式クレン運転技能講習'),
        ('高所作業車運転技能講習', '高所作業車運転技能講習'),
        ('技能講習6', '技能講習6'),
        ('技能講習7', '技能講習7'),
        ('技能講習8', '技能講習8'),
        ('技能講習9', '技能講習9'),
        ('技能講習10', '技能講習10'),
        ('技能講習11', '技能講習11'),
        ('技能講習12', '技能講習12'),
        ('技能講習13', '技能講習13'),
        ('技能講習14', '技能講習14'),
        ('技能講習15', '技能講習15'),
        ('技能講習16', '技能講習16'),
        ('技能講習17', '技能講習17'),
        ('技能講習18', '技能講習18'),
        ('技能講習19', '技能講習19'),
        ('技能講習20', '技能講習20'),
    ]
    man = models.OneToOneField(SoenMemberM, on_delete=models.PROTECT, related_name='soenmemberSkill', default='')
    skill_name = models.CharField(verbose_name="技能講習", max_length=30, null=True, blank=True, choices=skillTraning_list)

    def __str__(self):
        return self.skill_name
    class Meta:
        verbose_name_plural = "技能講習"



class LicenceM(models.Model):
    licence_list = [
        ('-', '-'),
        ('1級建築士', '1級建築士'),
        ('2級建築士', '2級建築士'),
        ('1級建築施工管理技士', '1級建築施工管理技士'),
        ('2級建築施工管理技士（建築）', '2級建築施工管理技士（建築）'),
        ('2級建築施工管理技士（仕上げ）', '2級建築施工管理技士（仕上げ）'),
        ('1級技能士　内装仕上げ施工（鋼製下地工事作業）', '1級技能士　内装仕上げ施工（鋼製下地工事作業）'),
        ('2級技能士　内装仕上げ施工（鋼製下地工事作業）', '2級技能士　内装仕上げ施工（鋼製下地工事作業）'),
        ('1級技能士　内装仕上げ施工（ﾎﾞｰﾄﾞ仕上げ工事作業）', '1級技能士　内装仕上げ施工（ﾎﾞｰﾄﾞ仕上げ工事作業）'),
        ('2級技能士　内装仕上げ施工（ﾎﾞｰﾄﾞ仕上げ工事作業）', '2級技能士　内装仕上げ施工（ﾎﾞｰﾄﾞ仕上げ工事作業）'),
        ('1級技能士　内装仕上げ施工（ﾌﾟﾗｽﾁｯｸ系床仕上げ工事作業）', '1級技能士　内装仕上げ施工（ﾌﾟﾗｽﾁｯｸ系床仕上げ工事作業）'),
        ('2級技能士　内装仕上げ施工（ﾌﾟﾗｽﾁｯｸ系床仕上げ工事作業）', '2級技能士　内装仕上げ施工（ﾌﾟﾗｽﾁｯｸ系床仕上げ工事作業）'),
        ('1級技能士　内装仕上げ施工（ｶｰﾍﾟｯﾄ系床仕上げ工事作業）', '1級技能士　内装仕上げ施工（ｶｰﾍﾟｯﾄ系床仕上げ工事作業）'),
        ('2級技能士　内装仕上げ施工（ｶｰﾍﾟｯﾄ系床仕上げ工事作業）', '2級技能士　内装仕上げ施工（ｶｰﾍﾟｯﾄ系床仕上げ工事作業）'),
        ('1級技能士　表装（表具作業）', '1級技能士　表装（表具作業）'),
        ('2級技能士　表装（表具作業）', '2級技能士　表装（表具作業）'),
        ('1級技能士', '1級技能士'),
        ('2級技能士', '2級技能士'),
        ('3級技能士', '3級技能士'),
        ('自動車運転免許', '自動車運転免許'),
        ('免許20', '免許20'),
    ]
    man = models.OneToOneField(SoenMemberM, on_delete=models.PROTECT, related_name='soenmemberLicence', default='')
    licence_name = models.CharField(verbose_name="免許", max_length=40, null=True, blank=True, choices=licence_list)

    def __str__(self):
        return self.licence_name
    class Meta:
        verbose_name_plural = "免許"

