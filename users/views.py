from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Acount Created for {}!'.format(username))
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
        template_name = 'users/register.html'
        return render(request,template_name, {'form':form})