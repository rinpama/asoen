from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from django.views.generic import TemplateView
from .forms import LoginForm

app_name='accounts'
# Create your views here.
class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class LoginTop(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/logtop.html'

class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/login.html'

from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError
@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)
