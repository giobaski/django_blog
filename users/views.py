from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your Account has been Created, dear {}! You are now able to log in'.format(username))
            return redirect('login')
    else:
        form = UserRegisterForm()
        template_name = 'users/register.html'
        return render(request,template_name, {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
