from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateMahasiswa
from .models import t_akun_mahasiswa
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        parameters = {
            'status' : 'logged out', 
        }
        return render(request, 'grader/home.html', parameters)
    else:
        parameters = {
            'status' : 'logged in', 
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

def BuatMhs(request):
    insert = CreateMahasiswa()
    if request.method == 'POST':
        insert = CreateMahasiswa(request.post)
        if insert.is_valid():
            insert.save()
            return render(request, 'grader/home.html')
        else:
            return HttpResponse("Gagal Brow")
