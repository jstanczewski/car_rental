from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm


class SubmittableLoginView(LoginView):
    template_name = 'accounts/form.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("index")
        else:
            print('Errors present!')

    else:
        form = SignUpForm()
    return render(request, 'accounts/form.html', {'form': form})
