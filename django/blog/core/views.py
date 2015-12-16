from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from core.forms import ProfileForm

def home(request):
    if request.user.is_authenticated():
        return render(request, 'core/index.html')
    else:
        return render(request, 'core/cover.html')

@login_required
def setting(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.profile.url = form.cleaned_data.get('url')
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            mesages.add_message(request, messages.SUCCESS, 'Your profile were successfully edited.')
        else:
            form = ProfileForm(
                instance=user,
                initial={
                    'url': user.profile.url,
                    'location': user.profile.location
                }
            )
        return render(request, 'core/setting.html', {'form':form})

@login_required
def picture(request):
    return render(request, 'core/setting.html')

@login_required
def password(request):
    return render(request, 'core/setting.html')
