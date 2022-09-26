from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from userapp.models import Muallif


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
            lo = request.POST.get('username')
            pa = request.POST.get('password')
            user = authenticate(username=lo, password=pa)
            if user is None:
                return redirect('/login/')
            else:
                login(request, user)
                return redirect('/')
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/login/')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        name = request.POST.get('name')
        passw = request.POST.get('pass_create')
        passw_repeat = request.POST.get('pass_repeat')
        if passw == passw_repeat:
            user = User.objects.create_user(username=name, password=passw)
            Muallif.objects.create(user=user, name=name)
            login(request, user)
            return redirect('/')
        else:
            return redirect('/register/')

