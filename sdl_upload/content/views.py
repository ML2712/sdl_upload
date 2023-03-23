from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

from .models import Client
from .forms import CreateUserForm
# Create your views here.


@admin_only
def home(request):
    context = {}
    return render(request, 'home.htm', context)


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='client')
            user.groups.add(group)
            Client.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.htm', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'login.htm', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def userPage(request):
    context = {}
    return render(request, 'user.htm', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def accountSettings(request):
    context = {}
    return render(request, 'account_set.htm', context)
