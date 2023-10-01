from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.

def register(request):
    if request.method == 'GET':
        register_form = RegisterForm()
        return render(request, 'users/register.html', {'register_form': register_form})

    register_form = RegisterForm(request.POST)

    if register_form.is_valid():
        register_form.save()
        return redirect('all_movies')
    else:
        return render(request, 'users/register.html', {'register_form': register_form})
