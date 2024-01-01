
# Create your views here.
from django.shortcuts import render
from .models import Profile
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from authentication.forms import UserForm
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserChangeForm, ProfilePictureForm

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        return render(request, 'profile.html', {'profile': profile})
    else:
        messages.error(request, 'Debes logearte para ver esta pagina.')
        return redirect('login')
    
def edit_profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user_id=request.user.id)
        form = CustomUserChangeForm(request.POST, instance=current_user)
        picture_form = ProfilePictureForm(request.POST, request.FILES, instance=profile)

        if request.method == 'POST':
            if form.is_valid() and picture_form.is_valid():
                form.save()
                picture_form.save()
                messages.success(request, 'Tu perfil ha sido actualizado.')
                return redirect('profile', pk=request.user.id)
        else:
            form = CustomUserChangeForm(instance=current_user)
            picture_form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        return render(request, 'edit_profile.html', {'form': form , 'picture_form': picture_form})
    else:
        messages.error(request, 'Debes logearte para ver esta pagina.')
        return redirect('login')
   
