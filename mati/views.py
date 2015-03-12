from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from forms import MyRegistrationForm


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect(reverse('loggedin'))
    else:
        return redirect('/accounts/invalid')


def loggedin(request):
    return render(request, 'loggedin.html')


def invalid_login(request):
    return render(request, 'invalid_login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')


def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()

            form.save()

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)

            return redirect('/accounts/register_success')

    else:
        form = MyRegistrationForm()

    args = dict(form=form)

    return render(request, 'register.html', args)


def register_success(request):
    return render(request, 'register_success.html')
