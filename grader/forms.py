from django import forms
from django.forms import ModelForm
from .models import t_akun_mahasiswa
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateMahasiswa(ModelForm):
    class Meta:
        model = t_akun_mahasiswa
        fields = ('__all__')

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    jenis = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ["username","email","password1","password2","jenis"]