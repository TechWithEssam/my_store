from django.shortcuts import render, redirect
from .forms import UserCreateProfile, LoginForm, UpdateProfileForm, UpdateInfo
from django.contrib.auth import login, logout
from datetime import date
from django.contrib import messages
from .models import User, Profile, Subscribe
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse


@login_required
def change_password_view(request):
    template_name = "users/change-password.html"
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST or None)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            # messages.success(request, 'Your password was successfully updated!')
            return redirect("users:my_profile")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, template_name, {"form":form})

def user_news_subscribe_view(request) :
    if request.method == "POST" :
        news_email = request.POST["news_email"]
        if not news_email :
            pass
        else :
            Subscribe(email=news_email).save()
    return redirect(request.META.get("HTTP_REFERER"))


def register_user_view(request) :
    template_name = "users/register.html"
    form = UserCreateProfile(request.POST or None)
    if form.is_valid() :
        date_of_birth = form.cleaned_data.get("date_of_birth")
        if date.today().year - date_of_birth.year > 18 :
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("/")
        else :
            messages.error(request, "Your age is not legal to register on our store")
    context = {
        "form":form
    }
    return render(request, template_name, context)

def login_user_view(request) :
    template_name = "users/login.html"
    form = LoginForm(request.POST, data=request.POST or None)
    if form.is_valid() :
        user = form.get_user()
        login(request, user)
        return redirect("/")
    context = {
        "form" : form
    }
    return render(request, template_name, context)


@login_required
def logout_user_view(request) :
    template_name = "users/logout.html"
    if request.method == "POST" :
        logout(request)
        return redirect("users:login")
    context = {}
    return render(request, template_name, context)


def my_profile_view(request) :
    template_name = 'users/my-profile.html'
    obj = Profile.objects.get(user=request.user)
    context = {
        "profile":obj
    }
    return render(request, template_name, context)

@login_required
def update_information_user(request) :
    user = request.user 
    template_name = "users/update.html"
    form = UpdateInfo(request.POST or None, instance=user)
    if form.is_valid() :
        form.save()
        return redirect("users:my_profile")
    context = {
        "form":form
    }
    return render(request, template_name, context)