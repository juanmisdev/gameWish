
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import redirect, render
from .models import Profile

class ProfilePictureForm(forms.ModelForm):
    picture = forms.ImageField(label='Foto de Perfil', widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        fields = ('picture',)

    def __init__(self, *args, **kwargs):
        super(ProfilePictureForm, self).__init__(*args, **kwargs)

        self.fields['picture'].widget.attrs['class'] = 'form-control'
        self.fields['picture'].label = 'Foto de Perfil'
        self.fields['picture'].help_text = '<span class="form-text text-muted"><small> Formatos: jpg, jpeg, png. Tamaño maximo: 2MB.</small></span>'


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = None

    
    class Meta:
        model = User
        fields = ('username', 'email')
        

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido. Menos de 150 caracteres. Letras, digitos y @/./+/-/_ estan permitidos.</small></span>'


        self.fields['email'].label = ''



