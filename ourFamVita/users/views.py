from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import UserManager
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm
from users.models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/profiles/")

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user_email = form.cleaned_data["user_email"]
            user_password = form.cleaned_data["user_password"]
            
            user = authenticate(username=user_email, password=user_password)
            if user:
                login(request, user)
                return redirect("/profiles/")
            else:
                form.add_error(None, "회원가입이 필요합니다.")
        
        context = {"form": form}
        return render(request, "users/login.html", context)
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "users/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/users/login/")


def signup(request):    
    if request.method == "POST":
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user_email = form.cleaned_data["user_email"]
            user_password = form.cleaned_data["user_password"]
            re_password = form.cleaned_data["re_password"]

        if User.objects.filter(user_email=user_email).exists():
                form.add_error("user_email", "중복된 이메일입니다.")
        
        if user_password != re_password:
                form.add_error("re_password", "비밀번호가 일치하지 않습니다.")

        if form.errors:
            context={"form": form}
            return render(request, "users/signup.html", context)
        
        else:
            user = User(user_email=user_email, user_password=user_password)
            user.save()
            login(request, user)
        return redirect("/")

    else:
        form = SignupForm()
        context = {"form": form}
        return render(request, "users/signup.html", context)



def acc_info(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PasswordChangeForm(user=request.user)

    context = {"form": form}
    return render(request, "users/acc_info.html", context)