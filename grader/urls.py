from django.urls import path
from django.conf.urls import url
from .views import home, loginView,logoutView,register, identif, matkulView, createMatkul, editMapel, nilaiMapel,deleteMapel, tambahNilai, beriNilai, editNilai, lihatNilai, datvis, datvisdos, datavisual, datavisualbesar
from . import views 

urlpatterns = [
    path('', views.home, name="home"), 
    url(r'^/login/$', loginView, name="login"),
    url(r'^/$', logoutView, name='logout'),
    url(r'^signup$', register, name='signup'),
    url(r'^/identify$', identif, name='iden'),
    url(r'^/matkul$', matkulView, name='dosen'),
    url(r'^/tambahMatkul$', createMatkul, name='tambahMatkul'),
    url(r'^editMatkul/(?P<pk>\d+)$', editMapel, name='editMapel'),
    url(r'^deleteMatkul/(?P<pk>\d+)$', deleteMapel, name='deleteMapel'),
    url(r'^nilai$', nilaiMapel, name='nilai'),
    url(r'^kasihNilai/(?P<kelas>\w+)/(?P<nm_map>\w+)/$', tambahNilai, name='beriNilai'),
    url(r'^tambahNilai/(?P<nama>[\w\ ]+)/(?P<kelas>\w+)/(?P<kode>\w+)$', beriNilai, name='tambahNilai'),
    url(r'^editNilai(?P<pk>\d+)$', editNilai, name='editNilai'),
    url(r'^lihatNilai(?P<username>\w+)$', lihatNilai, name='lihatNilai'),
    url(r'^dataVisualisasi(?P<id>\d+)$', datvis, name='datavis'),
    url(r'^dataVisualisasiDosen(?P<id>\w+)$', datvisdos, name='datvisdos'),
    url(r'^dataVisualisasiNilai(?P<id>\w+)$', datavisual, name='datanilai'),
    url(r'^dataVisual(?P<id>\w+)$', datavisualbesar, name='databesar'),
]