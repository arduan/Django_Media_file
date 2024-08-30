# my_app/views.py
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile


def upload_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm()
    return render(request, 'my_app/upload_profile.html', {'form': form})


def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'my_app/profile_list.html', {'profiles': profiles})
