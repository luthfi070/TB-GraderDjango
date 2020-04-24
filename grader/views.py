from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CreateMahasiswa, RegisterForm, Jenis, CreateMatkul, CreateNilai
from .models import t_akun_mahasiswa,t_pengguna, t_matkul, t_nilai
from django.db.models import Avg
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        usrn = request.user.username
        parameters = {
            'status' : 'logged in', 
        }
        tipe = t_pengguna.objects.filter(username=usrn, tipe='Dosen').exists()
        if tipe == True:
            parameters = {
                'tipe' : 'dosen',
                'status2' : 'verifikasi',
                'pengguna' : t_pengguna.objects.filter(username=usrn),
            }
        else:
            parameters = {
                'tipe' : 'mahasiswa',
                'status2' : 'verifikasi',
                'pengguna' : t_pengguna.objects.filter(username=usrn), 
            }
        return render(request, 'grader/home.html', parameters)
    else:
        usrn = request.user.username
        parameters = {
            'status' : 'logged out', 
            'pengguna' : t_pengguna.objects.filter(username=usrn)
        }
        return render(request, 'grader/home.html', parameters)
    
def loginView(request):
    context={
        'page_title':'LOGIN',
    }
    if request.method == "POST":
        
        username_lgn = request.POST['username']
        password_psw = request.POST['password']

        user = authenticate(request, username=username_lgn, password=password_psw)

        if user is not None:
            login(request,user)
            context={
        'status5' : 'logged in',
        }
        else:
            return redirect('login')
        return redirect('home')

    return render(request, 'grader/login.html', context)

def logoutView(request):
    context = {
        'page_title':'logout'
    }

    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)
            
        return redirect('home')
    return render(request, 'grader/logout.html', context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect('signup')
        return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'grader/signup.html', {"form" : form})

def identif(request):
    if request.method == "POST":
        form = Jenis(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = Jenis()
        return render(request, 'grader/identif.html', {'form' : form, 'pengguna' : t_pengguna.objects.all()})

def matkulView(request):
    return render(request, 'grader/matkul.html', {'matpel' : t_matkul.objects.all()})

def createMatkul(request):
    if request.method == "POST":
        form = CreateMatkul(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = CreateMatkul(request.POST)
        return render(request, 'grader/tambahMatkul.html', {'form' : form})

def editMapel(request, pk):
    mapel = get_object_or_404(t_matkul, pk=pk)
    status = 'success'
    titleValue = t_matkul.objects.filter(pk=pk).values('nama_mapel')[0];
    mapel_title = titleValue['nama_mapel']
    
    if request.method == 'POST':
        post_form = CreateMatkul(request.POST, instance=mapel)
        if post_form.is_valid():
            post_form.save()
            return redirect('dosen')
    else:
        form = CreateMatkul(instance=mapel)
        return render(request, 'grader/editMatpel.html', {'form': form, 'nama_mapel': mapel_title })

def deleteMapel(request, pk):
    mapel = t_matkul.objects.get(pk=pk)
    mapel.delete()
    return redirect('dosen')

def nilaiMapel(request):
    nama = request.user.username
    return render(request, 'grader/lihatMapel.html', {'matpel' : t_matkul.objects.filter(username_dosen=nama)})

def tambahNilai(request, kelas, nm_map):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        print(nama)
        return render(request, 'grader/beriNilai.html', {'matpel' : t_pengguna.objects.filter(kelas=kelas), 'nilai' : t_nilai.objects.filter(nama=nama).filter(kode_mapel=nm_map), 'nama' : t_matkul.objects.filter(kode_mapel=nm_map)})
    return render(request, 'grader/beriNilai.html', {'matpel' : t_pengguna.objects.filter(kelas=kelas), 'nama' : t_matkul.objects.filter(kode_mapel=nm_map)})

def beriNilai(request, nama, kelas, kode):
    print(nama)
    print(kelas)
    nama_a = t_pengguna.objects.filter(nama_lengkap=nama, kelas=kelas).values('nama_lengkap')[0]
    nama_title = nama_a['nama_lengkap']
    kelas_a = t_pengguna.objects.filter(nama_lengkap=nama, kelas=kelas).values('kelas')[0]
    kelas_title = kelas_a['kelas']
    namam_a = t_matkul.objects.filter(kode_mapel=kode).values('nama_mapel')[0]
    namam_title = namam_a['nama_mapel']
    kodem_a = t_matkul.objects.filter(kode_mapel=kode).values('kode_mapel')[0]
    kodem_title = kodem_a['kode_mapel']
    print(nama_a)
    if request.method == "POST":
        form = CreateNilai(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = CreateNilai(request.POST)
        return render(request, 'grader/tambahNilai.html', {'form' : form, 'nama' : nama_title, 'kelas' : kelas_title, 'namam' : namam_title, 'kodem' : kodem_title})

def editNilai(request, pk):
    mapel = get_object_or_404(t_nilai, pk=pk)
    status = 'success'
    titleValue = t_nilai.objects.filter(pk=pk).values('nilai')[0];
    mapel_title = titleValue['nilai']
    
    if request.method == 'POST':
        post_form = CreateNilai(request.POST, instance=mapel)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    else:
        form = CreateNilai(instance=mapel)
        return render(request, 'grader/editNilai.html', {'form': form, 'nama_mapel': mapel_title })

def lihatNilai(request, username):
    nilai = t_nilai.objects.filter(nama=username)
    id = t_nilai.objects.filter(nama=username).values('id')[0]
    id_title = id['id']
    return render(request, 'grader/lihatNilai.html', {'nilai' : nilai, 'id' : id_title})

def datvis(request, id):
    fruits = []
    counts = []
    usrn = request.user.username
    panjang = t_nilai.objects.filter(nama=usrn).count()
    for m in range (panjang):
        data = t_nilai.objects.filter(nama=usrn).values('nama_mapel')[m];
        mapel_title = data['nama_mapel']
        fruits.append(mapel_title)
        data2 = t_nilai.objects.filter(nama=usrn).values('nilai')[m];
        nama_title = data2['nilai']
        counts.append(nama_title)

    source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))

    p = figure(x_range=fruits, plot_height=350, toolbar_location=None, title="Data Nilai Kelas")
    p.vbar(x='fruits', top='counts', width=0.9, source=source, legend_field="fruits",
        line_color='white', fill_color=factor_cmap('fruits', palette=Spectral6, factors=fruits))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = 100
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    script, div = components(p)

    return render(None, 'grader/dataVisualisasi.html', {'script' : script, 'div' : div} )

def datvisdos(request, id):
    fruits = []
    counts = []
    panjang = t_nilai.objects.filter(kode_mapel=id).count()
    for m in range (panjang):
        data = t_nilai.objects.filter(kode_mapel=id).values('nama')[m];
        mapel_title = data['nama']
        fruits.append(mapel_title)
        data2 = t_nilai.objects.filter(kode_mapel=id).values('nilai')[m];
        nama_title = data2['nilai']
        counts.append(nama_title)

    source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))

    p = figure(x_range=fruits, plot_height=350, toolbar_location=None, title="Data Nilai")
    p.vbar(x='fruits', top='counts', width=0.9, source=source, legend_field="fruits",
        line_color='white', fill_color=factor_cmap('fruits', palette=Spectral6, factors=fruits))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = 100
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    script, div = components(p)

    return render(None, 'grader/dataVisualiasiDosen.html', {'script' : script, 'div' : div} )

def datavisual(request, id):
    fruits = []
    counts = []
    panjang = t_nilai.objects.filter(kode_mapel=id, nilai__gte='20', nilai__lte='50' ).count()
    print(panjang)
    for m in range (panjang):
        data = t_nilai.objects.filter(kode_mapel=id, nilai__gte='20', nilai__lte='50' ).values('nama')[m];
        mapel_title = data['nama']
        fruits.append(mapel_title)
        data2 = t_nilai.objects.filter(kode_mapel=id, nilai__gte='20', nilai__lte='50' ).values('nilai')[m];
        print(data2)
        nama_title = data2['nilai']
        counts.append(nama_title)

    source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))

    p = figure(x_range=fruits, plot_height=350, toolbar_location=None, title="Data Nilai")
    p.vbar(x='fruits', top='counts', width=0.9, source=source, legend_field="fruits",
        line_color='white', fill_color=factor_cmap('fruits', palette=Spectral6, factors=fruits))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = 100
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    script, div = components(p)

    return render(None, 'grader/DataVisualisasiNilai.html', {'script' : script, 'div' : div})

def datavisualbesar(request, id):
    fruits = []
    counts = []
    panjang = t_nilai.objects.filter(kode_mapel=id, nilai__gte='50', nilai__lte='150' ).count()
    print(panjang)
    for m in range (panjang):
        data = t_nilai.objects.filter(kode_mapel=id, nilai__gte='80', nilai__lte='150' ).values('nama')[m];
        print(data)
        mapel_title = data['nama']
        fruits.append(mapel_title)
        data2 = t_nilai.objects.filter(kode_mapel=id, nilai__gte='80', nilai__lte='150' ).values('nilai')[m];
        print(data2)
        nama_title = data2['nilai']
        counts.append(nama_title)

    source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))

    p = figure(x_range=fruits, plot_height=350, toolbar_location=None, title="Data Nilai")
    p.vbar(x='fruits', top='counts', width=0.9, source=source, legend_field="fruits",
        line_color='white', fill_color=factor_cmap('fruits', palette=Spectral6, factors=fruits))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = 100
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    script, div = components(p)

    return render(None, 'grader/DataVisualisasiBesar.html', {'script' : script, 'div' : div})

