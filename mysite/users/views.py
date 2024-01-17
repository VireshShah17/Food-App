from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request=request, message=f'Welcome {username}, you are registered successfully!')
            return redirect('users:login')
    else:
        form = RegisterForm()
    return render(request=request, template_name='users/register.html', context={'form': form})


@login_required
def profile(request):
    return render(request=request, template_name='users/profile.html')
