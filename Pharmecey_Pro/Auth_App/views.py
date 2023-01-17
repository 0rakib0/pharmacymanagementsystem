from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import UserProfile
from django.contrib import messages
# Create your views here.

def User_Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Success!')
            return redirect('Pharmacey_App:Deshbord')
        else:
            messages.error(request, 'username & password not match!')
        


    return render(request, 'Auth_App/login.html')

def User_Logout(request):
    logout(request)
    return redirect('Auth_app:login')


def User_Profile(request, id):
    profile = UserProfile.objects.filter(user=request.user)
    context = {
        'profile':profile
    }
    return render(request, 'Auth_app/userprofile.html', context)


def Edit_Profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    context = {
        'user_profile':user_profile
    }
    
    return render(request, 'Auth_app/edit_profile.html', context)


def Update_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        profile_pic = request.FILES.get('profile_pic')
        address = request.POST.get('address')

        user = User.objects.get(id=request.user.id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        userprofile = UserProfile.objects.get(user=request.user)
        if profile_pic is not None:
            userprofile.profile_pic = profile_pic
        userprofile.dob = dob
        userprofile.phone = phone
        userprofile.addess = address
        userprofile.save()
        messages.success(request, 'Profile Successfully Updated!')
        return redirect('Auth_app:edit_profile')
    return None


def Change_password(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = User.objects.get(id=request.user.id)
        print(user)
        if password1 == password2:
            user.set_password(password1)
            user.save()
            messages.success(request, 'Password successfully Changed!')
            return redirect('Auth_app:logout')
    return redirect('Auth_app:edit_profile')