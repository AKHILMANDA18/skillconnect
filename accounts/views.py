from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


# ================= REGISTER =================
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # After successful registration go to login page
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# ================= LOGIN =================
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.user_type == "freelancer":
                return redirect("freelancer_dashboard")
            else:
                return redirect("recruiter_dashboard")

    return render(request, "login.html")


# ================= LOGOUT =================
def user_logout(request):
    logout(request)
    return redirect("login")


# ================= DASHBOARDS =================
@login_required
def freelancer_dashboard(request):
    return render(request, "freelancer_dashboard.html")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.user_type == "freelancer":
                return redirect("freelancer_dashboard")
            else:
                return redirect("recruiter_dashboard")

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def freelancer_dashboard(request):
    return render(request, "freelancer_dashboard.html")


@login_required
def recruiter_dashboard(request):
    return render(request, "recruiter_dashboard.html")
@login_required
def recruiter_dashboard(request):
    return render(request, "recruiter_dashboard.html")