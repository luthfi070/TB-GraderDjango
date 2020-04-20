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
        ('SI4301','SI4301'),
        ('SI4302','SI4302'),
        ('SI4303','SI4303'),
        ('SI4304','SI4304'),
    )
    def __unicode__(self):
        return self.username

class t_pengguna(models.Model):
    username = models.CharField(max_length=15)
    tipe = models.CharField(max_length=15)
    KELAS_CHOICES = (
        ('SI4301','SI4301'),
        ('SI4302','SI4302'),
        ('SI4303','SI4303'),
    )
    kelas = models.CharField(max_length=15, choices=KELAS_CHOICES, default='SI4301')
    nama_lengkap = models.CharField(max_length=50, default='nama')

    def __unicode__(self):
        return self.username

class t_matkul(models.Model):
    nama_mapel = models.CharField(max_length=50)
    kode_mapel = models.CharField(max_length=20, default='kode')
    username_dosen = models.CharField(max_length=15)
    KELAS_CHOICES = (
        ('SI 43 01','SI 43 01'),
        ('SI 43 02','SI 43 02'),
        ('SI 43 03','SI 43 03'),
    )
    kelas = models.CharField(max_length=15, choices=KELAS_CHOICES, default='SI 43 01')
    nama_dosen = models.CharField(max_length=50, default='nama')
    
    def __unicode__(self):
        return self.username

class t_nilai(models.Model):
    nilai = models.CharField(max_length=5)
    NILAI_CHOICES = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
    )
    index = models.CharField(max_length=5, choices=NILAI_CHOICES, default='A')
    nama = models.CharField(max_length=50)
    KELAS_CHOICES = (
        ('SI 43 01','SI 43 01'),
        ('SI 43 02','SI 43 02'),
        ('SI 43 03','SI 43 03'),
    )
    kelas = models.CharField(max_length=15, choices=KELAS_CHOICES, default='SI 43 01')
    nama_mapel = models.CharField(max_length=50)
    kode_mapel = models.CharField(max_length=15, default='kode')

    def __unicode(self):
        return self.nilai





