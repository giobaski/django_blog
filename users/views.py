from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    form = UserCreationForm()
    template_name = 'users/register.html'
    return render(request,template_name, {'form':form})