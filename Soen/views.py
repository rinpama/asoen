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
class SoenMemberDeleteView(DeleteView,LoginRequiredMixin):
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

######################################################################
@login_required()
def UpdateMemberView(request, number):
    # data = get_object_or_404(SoenMemberM, id=number)
    data = SoenMemberM.objects.get(pk=number)
    data2 = data.soenmemberD
    if request.method == 'POST':
        form = SoenMemberF(request.POST, instance=data)
        form2 = soenmemberDetailF(request.POST, instance=data2)
        if all((form.is_valid(),form2.is_valid())):
            member=form.save()
            detail=form2.save(commit=False)
            detail.man=member
            detail.save()
            return redirect('Soen:loginmemberlist')
    else:
        form = SoenMemberF(instance=data)
        form2 = soenmemberDetailF(instance=data2)
    return render(request, 'Soen/logmemberupdate.html', {'form': form, 'data':data, 'form2': form2})

######################################################################
@login_required()
def DetailMember(request, number):
    data = SoenMemberM.objects.get(pk=number)
    # data2 = soenmemberDetailM(man=data)
    params = {
        'data': data,
        # 'data2': data2,
    }
    return render(request, 'Soen/logmemberdetail.html', params)

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
class soenmemberDetail(DetailView):
    model = SoenMemberM
    context_object_name = 'MemberD'
    template_name = 'Soen/soenmemberDetail.html'

class soenmemberHealth(DetailView):
    model = SoenMemberM
    context_object_name = 'MemberH'
    template_name = 'Soen/create/health.html'

class soenmemberVehicle(DetailView):
    model = SoenMemberM
    context_object_name = 'MemberV'
    template_name = 'Soen/create/vehicle.html'

class soenmemberInsurance(DetailView):
    model = SoenMemberM
    context_object_name = 'MemberI'
    template_name = 'Soen/create/insurance.html'

class soenmemberEducationSkillLicence(DetailView):
    model = SoenMemberM
    context_object_name = 'MemberS'
    template_name = 'Soen/create/skill.html'
