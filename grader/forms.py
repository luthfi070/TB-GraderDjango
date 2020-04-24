from django import forms
from django.forms import ModelForm
from .models import t_akun_mahasiswa, t_pengguna, t_matkul, t_nilai
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateMahasiswa(ModelForm):
    class Meta:
        model = t_akun_mahasiswa
        fields = ('__all__')

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","email","password1","password2","first_name","last_name"]

class Jenis(ModelForm):
    class Meta:
        model = t_pengguna
        fields = ['tipe','username','kelas','nama_lengkap']

class CreateMatkul(ModelForm):
    class Meta:
        model = t_matkul
        fields = ['nama_mapel','kode_mapel','username_dosen','kelas','nama_dosen']

class CreateNilai(ModelForm):
    class Meta:
        model = t_nilai
        fields = ['nilai','index','nama','kelas','nama_mapel','kode_mapel']
    