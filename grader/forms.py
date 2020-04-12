from django import forms
from django.forms import ModelForm
from .models import t_akun_mahasiswa

class CreateMahasiswa(ModelForm):
    class Meta:
        model = t_akun_mahasiswa
        fields = ('__all__')