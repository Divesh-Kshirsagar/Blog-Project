from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password

User = get_user_model()

app_name = 'MyUsers'

def Register(request):
    if request.user.is_authenticated:  # Correct check for authentication
        return redirect('Blogs:home')
    else:
        if request.method == 'POST':
            data = request.POST
            username = data.get('user_name')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password')
            confirm_password = data.get('confirm_password')
            
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists.')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already registered.')
                else:
                    user = User.objects.create(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=make_password(password)  # Hash password
                    )
                    user.save()
                    messages.success(request, 'Account created successfully.')
                    return redirect('Blogs:create')
            else:
                messages.warning(request, 'Passwords do not match.')
        return render(request, "MyUsers/register.html")


def login_page(request):
    if request.user.is_authenticated:  # Correct check for authentication
        return redirect('Blogs:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('user_name')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('Blogs:myblogs')
            else:
                messages.error(request, 'The username or password is incorrect.')
                return redirect("MyUsers:login")
        return render(request, "MyUsers/login.html")


def logout_page(request):
    logout(request)
    return redirect("Blogs:home")
