from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import NiñeraForm,ClienteForm,RegisterForm
from .models import *

def index(request):
    context = {}
    return render(request, 'mainapp/index.html', context)


def logueo(request):
    
    if request.user.is_authenticated:
        messages.success(request,'Ya estas conectado!')
        return redirect('index')

    if request.method == 'POST':
        user = request.POST.get('usuario')
        password = request.POST.get('password')
        usuario = authenticate(username=user, password=password) # aca estaba el error 'user'
        if usuario:
            login(request,usuario)
            return redirect('index')
        else:
            messages.info(request,'Debes registrarte')
            return redirect('registro')
    return render(request,'mainapp/logueo.html',{})


def log_out(request):
    if not request.user.is_authenticated:
        messages.error(request,'No se puede ir a la direccion')
        return redirect('index')
    else:
        logout(request)

    messages.success(request,'Sesion cerrada exitosamente')
    return redirect('index')

def register(request):

    if request.user.is_authenticated:
        messages.error(request,'Ya eres un usuario')
        return redirect('index')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request,user)
            messages.success(request,'Usuario creado exitosamente')
            return redirect('index')

    return render(request,'mainapp/registro.html',{'form' : form})


@login_required(login_url='logueo')
def register_niñera(request,user):

    form = NiñeraForm()

    if not request.user.is_authenticated:
        messages.error(request,'No se puede ir a la direccion')
        return redirect('index')

    if request.method == 'POST':
        form = NiñeraForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            perfil_niñera = User.objects.get(username = request.user.username)
            form.perfil_niñera = perfil_niñera
            if not is_niñera(user):
                if form.perfil_niñera not in Niñera.objects.all():
                    form.save()
                    messages.success(request, message='Registro como niñera exitoso!')
                    return redirect('index')  # access granted
            else:
                messages.error(request, message='Esta niñera ya se encuentra registrada')
                return redirect('index')    

        else:
            messages.error(request, message='Ha ocurrido un error con los campos a llenar.')
    else:
        form = NiñeraForm()
    return render(request, 'mainapp/register_niñera.html', {'form_niñera':form})

def is_niñera(user_identification):
    return Niñera.objects.filter(perfil_niñera=user_identification)


@login_required(login_url='logueo')
def register_cliente(request,user):
   
    form = ClienteForm()

    if not request.user.is_authenticated:
        messages.error(request,'No se puede ir a la direccion')
        return redirect('index')

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            perfil_cliente = User.objects.get(username = request.user.username)
            form.perfil_cliente = perfil_cliente
            if not is_cliente(user):
                if form.perfil_cliente not in Cliente.objects.all():
                    form.save()
                    messages.success(request, message='Registro como cliente exitoso!')
                    return redirect('index')
                else:
                    messages.error(request, message='Este cliente ya se encuentra registrado')
                    return redirect('index')
            else:
                messages.error(request, message='Ya tienes un perfil creado')
                return redirect('index')    
        else:
            messages.error(request, message='Ha ocurrido un error con los campos a llenar.')

    else:
        pass
    return render(request, 'mainapp/register_cliente.html', {'form_cliente':form})

def is_cliente(user_identification):
    return Cliente.objects.filter(perfil_cliente=user_identification)






# from django.shortcuts import redirect,render
# from .forms import CuidadorForm,OwnerKidForm
# from .models import *
# # Create your views here.
# def index(request):
#     return render(request,'Homepage/index.html',{})

# def cuidadora(request):
    
#     form = CuidadorForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form = form.save(commit=False)
#         user = User.objects.get(username = request.user.username)
#         form.user_id = user
#         if form.user_id not in Cuidadora.objects.all():
#             if is_valid_ownerkid(user):
#                 form.save()
#                 return redirect('home:index')
#             else:
#                 return redirect('user:logout')
#         else:
#             return redirect('user:logout')
#     else:
#         form = CuidadorForm(request.POST or None)
#     return render(request,'reservation/change_cuid.html',{'form':form})

# def ownerkid(request):
    
#     form = OwnerKidForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form = form.save(commit=False)
#         user = User.objects.get(username = request.user.username)
#         form.user_id = user
#         if form.user_id not in Cuidadora.objects.all():
#             if is_valid_ownerkid(user):
#                 form.save()
#                 return redirect('home:index')
#             else:
#                 return redirect('user:logout')
#         else:
#             return redirect('user:logout')
#     else:
#         form = OwnerKidForm(request.POST or None)
#     return render(request,'reservation/ownerkid.html',{'form':form})
# def is_valid_cuidador(user_name):
#     return not Cuidadora.objects.filter(user_id=user_name) 

# def is_valid_ownerkid(user_name):
#     return not OwnerKid.objects.filter(user_id=user_name