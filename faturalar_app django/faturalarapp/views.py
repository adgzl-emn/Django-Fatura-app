from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Faturalar
from .forms import ListForm
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User


@login_required(login_url='/login')
def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            fatura_list = Faturalar.objects.all()
            return render(request,"faturalarapp/index.html",{'fatura_list':fatura_list})
    else:
        fatura_list = Faturalar.objects.all()
        return render(request,"faturalarapp/index.html",{'fatura_list':fatura_list})

def about(request):
    return render(request,"faturalarapp/about.html")


def create(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            return redirect("index")
            fatura_list = Faturalar.objects.all()
            return render(request,"faturalarapp/create.html",{'fatura_list':fatura_list})
            
    else:
        fatura_list = Faturalar.objects.all()
        return render(request,"faturalarapp/create.html",{'fatura_list':fatura_list})
        

def delete(request,Faturalar_id):
    fatura = Faturalar.objects.get(pk=Faturalar_id)
    fatura.delete()
    return redirect("index")


def yes_finish(request,Faturalar_id):
    fatura = Faturalar.objects.get(pk=Faturalar_id)
    fatura.odendi = False
    fatura.save()
    return redirect("index")


def no_finish(request,Faturalar_id):
    fatura = Faturalar.objects.get(pk=Faturalar_id)
    fatura.odendi = True  
    fatura.save()
    return redirect("index")


def update(request,Faturalar_id):
    if request.method == "POST":
        fatura_list = Faturalar.objects.get(pk=Faturalar_id)
        form = ListForm(request.POST or None,instance=fatura_list)
        if form.is_valid:
            form.save()
            return redirect("index")
    else:
        fatura_list = Faturalar.objects.all()
        return render(request,"faturalarapp/update.html",{'fatura_list':fatura_list})


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			messages.success(request, "Başarıyla kaydolundu!" )
			return redirect("login")
		messages.error(request, "Kayıt Başarısız.")
	form = NewUserForm
	return render (request=request, template_name="main/register.html", context={"register_form":form})   

def login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				auth_login(request,user)
				messages.info(request, f"{username} olarak giriş yaptın.")
				return redirect("index")
			else:
				messages.error(request,"Geçersiz Kullanıcı adı ve şifre.")
		else:
			messages.error(request,"Geçersiz Kullanıcı adı ve şifre.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})
	
def users(request):
        user_list = User.objects.all()
        return render(request,"faturalarapp/users.html",{'user_list':user_list})

def about(request):
    return render(request,"faturalarapp/about.html")

		
def logout(request):
    django_logout(request)
    return  redirect('login')
