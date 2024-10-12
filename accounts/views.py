from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm    
from .forms import RegisterForm

def homePage(request):
    return render(request, "home.html")


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Nie udało się zalogować użytkownika.",extra_tags="danger")
    context = {'form': form}
    return render(request, "accounts/loginPage.html", context)


@login_required
def logoutUser(request):
    logout(request)
    messages.success(request,"Wylogowano pomyślnie.",extra_tags="success")
    return redirect('login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        form.fields['email'].required = True
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request, "użytkownik zarejestrowany", extra_tags="success")
            return redirect('login')

    context = {'form': form}
    return render(request, "accounts/registerPage.html", context)
