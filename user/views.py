from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required(login_url="/signin")
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Hi {username}, your account was created successfully!')

            return redirect('signin')
    else:
        form = SignUpForm()

    return render(request, 'user/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            messages.warning(request, 'Username or password is incorrect')
    else:
        pass

    return render(request, 'user/signin.html')


def logout_view(request):
    logout(request)
    return render(request, 'home.html')
