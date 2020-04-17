from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your models here.
class t_akun_mahasiswa(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    jurusan = models.CharField(max_length=20)
    KELAS_CHOICES = (
        ('SI 43 01','SI 43 01'),
        ('SI 43 02','SI 43 02'),
        ('SI 43 03','SI 43 03'),
        ('SI 43 04','SI 43 04'),
    )
    def __unicode__(self):
        return self.username

class t_pengguna(models.Model):
    username = models.CharField(max_length=15)
    tipe = models.CharField(max_length=15)
    kelas = models.CharField(max_length=15)

    def __unicode__(self):
        return self.username

class t_matkul(models.Model):
    nama_mapel = models.CharField(max_length=50)
    username_dosen = models.CharField(max_length=15)
    KELAS_CHOICES = (
        ('SI 43 01','SI 43 01'),
        ('SI 43 02','SI 43 02'),
        ('SI 43 03','SI 43 03'),
    )
    kelas = models.CharField(max_length=15, choices=KELAS_CHOICES, default='SI 43 01')
    
    def __unicode__(self):
        return self.username




