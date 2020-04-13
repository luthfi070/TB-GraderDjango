from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateMahasiswa, RegisterForm, Jenis
from .models import t_akun_mahasiswa, t_pengguna
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        parameters = {
            'status' : 'logged in', 
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

def BuatMhs(request):
    insert = CreateMahasiswa()
    if request.method == 'POST':
        insert = CreateMahasiswa(request.post)
        if insert.is_valid():
            insert.save()
            return render(request, 'grader/home.html')
        else:
            return HttpResponse("Gagal Brow")
