from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import GenreM, SoenMemberM, soenmemberDetailM, VehicleM, SpecialEducationM, HealthM, InsuranceM, SkillM, \
    LicenceM
from .forms import GenreF, SoenMemberF, soenmemberDetailF, VehicleF, SpecialEducationF, HealthF, InsuranceF, SkillF, \
    LicenceF


######################################################################
# DeleteMember
class SoenMemberDeleteView(DeleteView, LoginRequiredMixin):
    template_name = 'Soen/logmemberdelete.html'
    model = SoenMemberM
    success_url = reverse_lazy('accounts:logintop')


######################################################################
# class UpdateMemberView(UpdateView):
#     template_name = 'Soen/logmemberupdate.html'
#     model = soenmemberDetailM
#     fields='__all__'
#     def get_success_url(self):
#         return reverse('Soen:detailmember',kwargs={'number':self.object.pk})

@login_required()
def UpdateMemberView(request, number):
    data = get_object_or_404(SoenMemberM, id=number)
    # data = SoenMemberM.objects.get(pk=number)
    data2 = data.soenmemberD
    if request.method == 'POST':
        form = SoenMemberF(request.POST, instance=data)
        form2 = soenmemberDetailF(request.POST, instance=data2)
        if all((form.is_valid(), form2.is_valid())):
            member = form.save()
            detail = form2.save(commit=False)
            detail.man = member
            detail.save()
            return redirect('Soen:loginmemberlist')
    else:
        form = SoenMemberF(instance=data)
        form2 = soenmemberDetailF(instance=data2)
    return render(request, 'Soen/logupdate/logmemberupdate.html', {'form': form, 'data': data, 'form2': form2})


@login_required()
def UpdateHealthView(request, number):
    data = SoenMemberM.objects.get(pk=number)
    data2 = data.soenmemberHealth
    if request.method == 'POST':
        form = SoenMemberF(request.POST, instance=data)
        form2 = HealthF(request.POST, instance=data2)
        if all((form.is_valid(), form2.is_valid())):
            member = form.save()
            detail = form2.save(commit=False)
            detail.man = member
            detail.save()
            return redirect('Soen:loginmemberlist')
    else:
        form = SoenMemberF(instance=data)
        form2 = HealthF(instance=data2)
    return render(request, 'Soen/logupdate/loghealthupdate.html', {'form': form, 'data': data, 'form2': form2})


@login_required()
def UpdateSkillView(request, number):
    data = SoenMemberM.objects.get(pk=number)
    data2 = data.soenmemberSkill
    data3 = data.soenmemberEducation
    data4 = data.soenmemberLicence
    if request.method == 'POST':
        form = SoenMemberF(request.POST,request.FILES, instance=data)
        form2 = SkillF(request.POST,request.FILES, instance=data2)
        form3 = SpecialEducationF(request.POST,request.FILES, instance=data3)
        form4 = LicenceF(request.POST,request.FILES, instance=data4)
        if all((form.is_valid(), form2.is_valid(), form3.is_valid(), form4.is_valid())):
            member = form.save()
            detail = form2.save(commit=False)
            detail2 = form3.save(commit=False)
            detail3 = form4.save(commit=False)
            detail.man = member
            detail2.man = member
            detail3.man = member
            detail.save()
            detail2.save()
            detail3.save()
            return redirect('Soen:loginmemberlist')
    else:
        form = SoenMemberF(instance=data)
        form2 = SkillF(instance=data2)
        form3 = SpecialEducationF(instance=data3)
        form4 = LicenceF(instance=data4)
    return render(request, 'Soen/logupdate/logskillupdate.html',
                  {'form': form, 'data': data, 'form2': form2, 'form3': form3, 'form4': form4})

@login_required()
def UpdateSpecialEducationOnly(request, number):
    data = SoenMemberM.objects.get(pk=number)
    data3 = data.soenmemberEducation
    if request.method == 'POST':
        form = SoenMemberF(request.POST,request.FILES, instance=data)
        form3 = SpecialEducationF(request.POST,request.FILES, instance=data3)
        if all((form.is_valid(), form3.is_valid(), )):
            member = form.save()
            detail2 = form3.save(commit=False)
            detail2.man = member
            detail2.save()
            return redirect('Soen:loginmemberlist')
    else:
        form = SoenMemberF(instance=data)
        form3 = SpecialEducationF(instance=data3)
    return render(request, 'Soen/logupdate/logspecialeducationonlyupdate.html',
                  {'form': form, 'data': data,  'form3': form3,})

@login_required()
def UpdateSkillOnly(request, number):
    data = SoenMemberM.objects.get(pk=number)
    data2 = data.soenmemberSkill
    if request.method == 'POST':
        form = SoenMemberF(request.POST,request.FILES, instance=data)
        form2 = SkillF(request.POST,request.FILES, instance=data2)
        if all((form.is_valid(), form2.is_valid())):
            member = form.save()
            detail = form2.save(commit=False)
            detail.man = member
            detail.save()
            return redirect('Soen:loginmemberlist')
    else:
        form = SoenMemberF(instance=data)
        form2 = SkillF(instance=data2)
    return render(request, 'Soen/logupdate/logskillonlyupdate.html',
                  {'form': form, 'data': data, 'form2': form2,})

@login_required()
def UpdateLicenceOnly(request, number):
    data = SoenMemberM.objects.get(pk=number)
    data4 = data.soenmemberLicence
    if request.method == 'POST':
        form = SoenMemberF(request.POST,request.FILES, instance=data)
        form4 = LicenceF(request.POST,request.FILES, instance=data4)
        if all((form.is_valid(), form4.is_valid())):
            member = form.save()
            detail3 = form4.save(commit=False)
            detail3.man = member
            detail3.save()
            return redirect('Soen:loginmemberlist')
    else:
        form = SoenMemberF(instance=data)
        form4 = LicenceF(instance=data4)
    return render(request, 'Soen/logupdate/loglicenceonlyupdate.html',
                  {'form': form, 'data': data, 'form4': form4})


@login_required()
def UpdateInsuranceView(request, number):
    data = SoenMemberM.objects.get(pk=number)
    data2 = data.soenmemberInsurance
    if request.method == 'POST':
        form = SoenMemberF(request.POST, instance=data)
        form2 = InsuranceF(request.POST, instance=data2)
        if all((form.is_valid(), form2.is_valid())):
            member = form.save()
            detail = form2.save(commit=False)
            detail.man = member
            detail.save()
            return redirect('Soen:loginmemberlist')
    else:
        form = SoenMemberF(instance=data)
        form2 = InsuranceF(instance=data2)
    return render(request, 'Soen/logupdate/loginsuranceupdate.html', {'form': form, 'data': data, 'form2': form2})


@login_required()
def UpdateVehicleView(request, number):
    vehicle = VehicleM.objects.get(pk=number)
    if request.method == 'POST':
        form2 = VehicleF(request.POST, instance=vehicle)
        if form2.is_valid():
            form2.save()
            return redirect('Soen:loginmemberlist')
    else:
        form2 = VehicleF(instance=vehicle)
    return render(request, 'Soen/logupdate/logvehicleupdate.html',
                  {'vehicle': vehicle, 'form2': form2})  # , 'data':data,


######################################################################
@login_required()
def LoginDetailMember(request, number):
    data = SoenMemberM.objects.get(pk=number)
    params = {
        'data': data,
    }
    return render(request, 'Soen/logdetail/logmemberdetail.html', params)


@login_required()
def LoginDetailHealth(request, number):
    data = SoenMemberM.objects.get(pk=number)
    params = {
        'data': data,
    }
    return render(request, 'Soen/logdetail/loghealthdetail.html', params)


@login_required()
def LoginDetailInsurance(request, number):
    data = SoenMemberM.objects.get(pk=number)
    params = {
        'data': data,
    }
    return render(request, 'Soen/logdetail/loginsurancedetail.html', params)


@login_required()
def LoginDetailSkill(request, number):
    data = SoenMemberM.objects.get(pk=number)
    params = {
        'data': data,
    }
    return render(request, 'Soen/logdetail/logskilldetail.html', params)


@login_required()
def LoginDetailVehicle(request, number):
    data = SoenMemberM.objects.get(pk=number)
    vehicle = data.vehiclem_set.filter(
        man__name=data.name)  # ==> vehicle = VehicleM.objects.filter(man__name=data.name)
    params = {
        'data': data,
        'vehicle': vehicle,
    }
    return render(request, 'Soen/logdetail/logvehicledetail.html', params)


######################################################################
@login_required()
def LoginMemberList(request):
    data = SoenMemberM.objects.filter(genre_id=1)
    params = {
        'data': data,
    }
    return render(request, 'Soen/loglist.html', params)


@login_required()
def LoginShokukataList(request):
    data = SoenMemberM.objects.filter(genre_id=2)
    params = {
        'data': data,
    }
    return render(request, 'Soen/loglist.html', params)


@login_required()
def LoginUncategoryList(request):
    data = SoenMemberM.objects.filter(genre_id=5)
    params = {
        'data': data,
    }
    return render(request, 'Soen/loglist.html', params)
@login_required()
def LoginVehicleList(request):
    data = VehicleM.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'Soen/logvehiclelist.html', params)


# *********************************** login before-after ***********************************************
class SoenTop(TemplateView):
    template_name = 'Soen/top.html'


######################################################################
class CreateMember(CreateView):
    model = SoenMemberM
    form_class = SoenMemberF
    template_name = 'Soen/createmember.html'

    def get_success_url(self):
        return reverse('Soen:soentop')


def CreateDetailMember(request, number):
    name = SoenMemberM.objects.get(pk=number)
    params = {
        'name': name.name,
        # 'form':soenmemberDetailF(instance=data),
        'form': soenmemberDetailF()
    }
    if (request.method == 'POST'):
        data = soenmemberDetailM(man_id=name.id)
        record = soenmemberDetailF(request.POST, instance=data)
        record.save()
        return redirect(to='Soen:soentop')
    return render(request, 'Soen/createdetailmember.html', params)


def CreateHealth(request, number):
    name = SoenMemberM.objects.get(pk=number)
    params = {
        'name': name.name,
        # 'form':soenmemberDetailF(instance=data),
        'form': HealthF()
    }
    if (request.method == 'POST'):
        data = HealthM(man_id=name.id)
        record = HealthF(request.POST, instance=data)
        record.save()
        return redirect(to='Soen:soentop')
    return render(request, 'Soen/createdetailmember.html', params)


def CreateInsurance(request, number):
    name = SoenMemberM.objects.get(pk=number)
    params = {
        'name': name.name,
        # 'form':soenmemberDetailF(instance=data),
        'form': InsuranceF()
    }
    if (request.method == 'POST'):
        data = InsuranceM(man_id=name.id)
        record = InsuranceF(request.POST, instance=data)
        record.save()
        return redirect(to='Soen:soentop')
    return render(request, 'Soen/createdetailmember.html', params)


# def CreateEducationSkillLicence(request, number):
#     name = SoenMemberM.objects.get(pk=number)
#     params = {
#         'name': name.name,
#         # 'form':soenmemberDetailF(instance=data),xxx
#         'form': SpecialEducationF(),
#         'form2': SkillF(),
#         'form3': LicenceF()
#     }
#     if (request.method == 'POST'):
#         name = SoenMemberM.objects.get(pk=number)
#         data = SpecialEducationM(man_id=name.id)
#         record = SpecialEducationF(request.POST,request.FILES, instance=data)
#         data2 = SkillM(man_id=name.id)
#         record2 = SkillF(request.POST,request.FILES, instance=data2)
#         data3 = LicenceM(man_id=name.id)
#         record3 = LicenceF(request.POST,request.FILES, instance=data3)
#         record.save()
#         record2.save()
#         record3.save()
#         return redirect(to='Soen:soentop')
#     return render(request, 'Soen/createdetailmember.html', params)

def CreateEducationSkillLicence(request,number):
    data=SoenMemberM.objects.get(pk=number)
    params={
        'data':data,
    }
    return render(request,'Soen/CreateEducationSkillLicence.html',params)

def CreateSpecialEducation(request, number):
    name = SoenMemberM.objects.get(pk=number)
    params = {
        'name': name,
        'form': SpecialEducationF()
    }
    if (request.method == 'POST'):
        speeduf=SpecialEducationF(request.POST)
        speedu=speeduf.save(commit=False)
        speedu.man=name
        speedu.save()
        return redirect(to='Soen:soentop')
    return render(request, 'Soen/createdetailmember.html', params)
def CreateSkill(request, number):
    name = SoenMemberM.objects.get(pk=number)
    params = {
        'name': name,
        'form': SkillF()
    }
    if (request.method == 'POST'):
        skillf=SkillF(request.POST)
        skil=skillf.save(commit=False)
        skil.man=name
        skil.save()
        return redirect(to='Soen:soentop')
    return render(request, 'Soen/createdetailmember.html', params)
def CreateLicence(request, number):
    name = SoenMemberM.objects.get(pk=number)
    params = {
        'name': name,
        'form': LicenceF()
    }
    if (request.method == 'POST'):
        licenf=LicenceF(request.POST)
        licen=licenf.save(commit=False)
        licen.man=name
        licen.save()
        return redirect(to='Soen:soentop')
    return render(request, 'Soen/createdetailmember.html', params)

def CreateVehicle(request):
    # name = SoenMemberM.objects.get(pk=number)
    params = {
        # 'name': name.name,
        # 'form':soenmemberDetailF(instance=data),
        'form': VehicleF()
    }
    if (request.method == 'POST'):
        # data = VehicleM(man_id=name.id)
        record = VehicleF(request.POST)#, instance=data
        record.save()
        return redirect(to='Soen:soentop')
    return render(request, 'Soen/createdetailmember.html', params)


######################################################################
class SoenMember(ListView):
    template_name = 'Soen/soenmember.html'
    context_object_name = 'Members'
    # model=SoenMemberM#queryset = SoenMemberM.objects.all()
    queryset = SoenMemberM.objects.filter(genre_id=1)


class ShokukataMember(ListView):
    template_name = 'Soen/soenmember.html'
    context_object_name = 'Members'
    queryset = SoenMemberM.objects.filter(genre_id=2)


class Uncategory(ListView):
    template_name = 'Soen/soenmember.html'
    context_object_name = 'Members'
    queryset = SoenMemberM.objects.filter(genre_id=5)


#################################################################################
def soenmemberDetail(request, number):
    MemberD = SoenMemberM.objects.get(pk=number)
    params = {'MemberD': MemberD, }
    return render(request, 'Soen/notlogdetail/soenmemberDetail.html', params)


def soenmemberHealth(request, number):
    MemberH = SoenMemberM.objects.get(pk=number)
    params = {'MemberH': MemberH, }
    return render(request, 'Soen/notlogdetail/health.html', params)


def soenmemberInsurance(request, number):
    MemberI = SoenMemberM.objects.get(pk=number)
    params = {'MemberI': MemberI, }
    return render(request, 'Soen/notlogdetail/insurance.html', params)


def soenmemberEducationSkillLicence(request, number):
    MemberS = SoenMemberM.objects.get(pk=number)
    params = {'MemberS': MemberS, }
    return render(request, 'Soen/notlogdetail/skill.html', params)


def soenmemberVehicle(request, number):
    MemberV = SoenMemberM.objects.get(pk=number)
    vehicle=MemberV.vehiclem_set.filter(man__name=MemberV.name)
    params = {
        'Memberv': MemberV,
        'vehicle':vehicle
    }
    return render(request, 'Soen/notlogdetail/vehicle.html', params)
