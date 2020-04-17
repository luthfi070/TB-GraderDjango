from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CreateMahasiswa, RegisterForm, Jenis, CreateMatkul
from .models import t_akun_mahasiswa,t_pengguna, t_matkul
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        parameters = {
            'status' : 'logged in', 
        }
        usrn = request.user.username
        tipe = t_pengguna.objects.filter(username=usrn, tipe='Dosen').exists()
        print(tipe)
        if tipe == True:
            parameters = {
                'tipe' : 'dosen',
                'status2' : 'verifikasi',
            }
        else:
            parameters = {
                'tipe' : 'mahasiswa',
                'status2' : 'verifikasi', 
            }
        return render(request, 'grader/home.html', parameters)
    else:
        parameters = {
            'status' : 'logged out', 
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

def BuatMhs(request):
    insert = CreateMahasiswa()
    if request.method == 'POST':
        insert = CreateMahasiswa(request.post)
        if insert.is_valid():
            insert.save()
            return render(request, 'grader/home.html')
        else:
            return HttpResponse("Gagal Brow")

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
