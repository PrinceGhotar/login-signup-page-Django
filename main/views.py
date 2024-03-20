from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Set a flag indicating successful registration
            request.session['registration_successful'] = True
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('https://genius.com/artists/Lush')
    return render(request, 'registration/login.html')


def password_recovery(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Send email with password recovery link
            send_mail(
                'Password Recovery',
                'Click the link to reset your password.',
                'admin@learn_django.com',
                [email],
                fail_silently=False,
            )
            return redirect('login')
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_recovery.html', {'form': form})
