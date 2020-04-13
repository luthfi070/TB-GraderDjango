from django import forms
from django.db import models


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

