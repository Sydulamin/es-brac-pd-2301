from django.contrib.auth import get_user_model, authenticate ,login , logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
User = get_user_model()


# Create your views here.


def home(r):
    return render(r, 'home.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Are Logged In')
            return redirect('home')
        else:
            messages.error(request, 'User Not Found.')
            return redirect('registration')
    return render(request, 'login.html')


def registration(r):
    if r.method == 'POST':
        name = r.POST.get('name')
        email = r.POST.get('email')
        password = r.POST.get('password')
        password1 = r.POST.get('password1')
        if password == password1:
            if User.objects.filter(username=name).exists():
                messages.error(r, 'User Name Already Exist.')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.set_password(password)
                user.save()
                messages.success(r, 'Profile details Created.')
                return redirect('login')
        else:
            messages.error(r, 'password did not matched.')
            return redirect('registration')
    return render(r, 'registration.html')


def log_out(request):
    logout(request)
    messages.error(request, 'User logged out.')
    return redirect('login')\


def change_pass(r):
    if r.method == 'POST':
        name = r.POST.get('name')
        email = r.POST.get('email')
        password = r.POST.get('password')
        if name:
            user = User.objects.get(username=name)
            if user.email == email:
                user.set_password(password)
                user.save()
                update_session_auth_hash(r, user)
                messages.error(r, 'User pass change success.')
                return redirect('login')
            else:
                messages.error(r, 'email not matched.')
    return render(r, 'pass_change.html')
