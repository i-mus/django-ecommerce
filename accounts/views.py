from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def register(request):
    if request.method == 'POST':
        un = request.POST.get('user_name')
        email = request.POST.get('email_id')
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if User.objects.filter(username=un).exists():
            messages.info(request, "username already exists")
            return redirect('accounts:register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "email already exist")
            return redirect('accounts:register')
        elif pass1 == pass2:
            user = User.objects.create_user(username=un, email=email, password=pass1, first_name=fn, last_name=ln)
            user.save()
            print('user created')
            return redirect('accounts:login')
        else:
            messages.info(request, 'passwords donot match')
            return redirect('accounts:register')
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        user = auth.authenticate(username=uname, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid user")
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('accounts:login')
