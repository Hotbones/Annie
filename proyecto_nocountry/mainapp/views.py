from multiprocessing import current_process
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import NiñeraForm,ClienteForm,RegisterForm,ReservationForm,MensajeForm
from .models import *

def index(request):
    perfil=None
    cliente=None
    niñera=None
    try:
        perfil = Niñera.objects.get(perfil_id=request.user.id)
        niñera = perfil
    except:
        pass
    try:
        perfil = Cliente.objects.get(perfil_id=request.user.id)
        cliente = perfil
    except:
        pass
    context = {'perfil':perfil,'niñera':niñera,'cliente':cliente}
    return render(request, 'mainapp/index.html', context)

def searcher(request):
    return render(request, 'mainapp/searcher.html', {})

@login_required(login_url='logueo')
def profiles(request,id,superfil=None,otro=None,puntaje=0):
    
    if Cliente.objects.filter(perfil_id = id).exists():
        superfil = Cliente.objects.get(perfil_id = id)
    elif Niñera.objects.filter(perfil_id = id).exists():
        superfil = Niñera.objects.get(perfil_id = id)
    usuario = User.objects.get(id=id)
    
    otro=User.objects.all()
    print(otro)

    if request.method == 'POST':
        form_comentario = MensajeForm(request.POST)
        
        # if form_comentario.is_valid():
        comentarista = request.user.username
        puntaje=str(puntaje)
        nuevo_comentario = request.POST['comment']
        c = Mensaje(usuario=usuario, comentarista=comentarista, puntaje=puntaje, mensaje=nuevo_comentario)
        c.save()
        messages.success(request, message='Comentario publicado')

    else:
        form_comentario = MensajeForm()


    context = {'usuario':usuario,'form_comentario':form_comentario,'superfil':superfil, 'otro':otro}
    return render(request, 'mainapp/profiles.html', context)


def logueo(request):
    
    if request.user.is_authenticated:
        messages.success(request,'Ya estas conectado!')
        return redirect('welcome')

    if request.method == 'POST':
        user = request.POST.get('usuario')
        password = request.POST.get('password')
        usuario = authenticate(username=user, password=password) # aca estaba el error 'user'
        if usuario:
            login(request,usuario)
            messages.success(request,'Bienvenido de nuevo'.format(usuario))
            return redirect('welcome')
        else:
            messages.info(request,'Debes registrarte')
            return redirect('registro')
    return render(request,'mainapp/logueo.html',{})


def log_out(request):
    if not request.user.is_authenticated:
        messages.error(request,'No se puede ir a la direccion')
        return redirect('index')
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

    if not request.user.is_authenticated:
        messages.error(request,'No se puede ir a la direccion')
        return redirect('index')
    if Niñera.objects.filter(perfil=request.user).exists() or Cliente.objects.filter(perfil=request.user).exists():
        messages.error(request, message='Ya has creado un perfil')
        return redirect('index')
    form = NiñeraForm()


    if request.method == 'POST':
        
        form = NiñeraForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            form.perfil = user
            form.save()
            messages.success(request, message='Registro como niñera exitoso!')
            return redirect('welcome')  # access granted
           
            
        else:
            messages.error(request, message='Ha ocurrido un error con los campos a llenar.')

    return render(request, 'mainapp/register_niñera.html',{
        'form': form
    })

@login_required(login_url='logueo')
def register_cliente(request,user):
   
    if Niñera.objects.filter(perfil=request.user).exists() or \
    Cliente.objects.filter(perfil=request.user).exists():
        messages.error(request, message='Ya has creado un perfil')
        return redirect('index')


    if not request.user.is_authenticated:
        messages.error(request,'No se puede ir a la direccion')
        return redirect('index')
    if Niñera.objects.filter(perfil=request.user).exists() or Cliente.objects.filter(perfil=request.user).exists():
        
            return redirect('index')
    form = ClienteForm()


    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            form.perfil = user
            form.save()
            messages.success(request, message='Registro como cliente exitoso!')
            return redirect('welcome')  # access granted     
        else:
            messages.error(request, message='Ha ocurrido un error con los campos a llenar.')
    else:
        form = ClienteForm()
    return render(request, 'mainapp/register_cliente.html', {'form_cliente':form})


@login_required(login_url='logueo')
def update_perfil(request,user):
    try:
        perfil = Niñera.objects.get(perfil_id=request.user.id)
        form = NiñeraForm(instance=perfil)
        if request.method == 'POST':
            form = NiñeraForm(request.POST, instance=perfil)
            form.save()
            messages.success(request, 'Perfil actualizado exitosamente!')
            return redirect('index')
    except:
        pass
    
    try:
        perfil = Cliente.objects.get(perfil_id=request.user.id)
        form = ClienteForm(instance=perfil)
        if request.method == 'POST':
            form = ClienteForm(request.POST, instance=perfil)
            form.save()
            messages.success(request, 'Perfil actualizado exitosamente!')
            return redirect('index')
    except:
        if perfil == None:
            print('aqui')
            messages.error(request,'No existe ningún perfil')
            return redirect('index')
        else:
            pass
    finally:
        if perfil == None:
            messages.error(request,'No se puede acceder')
        context = {'perfil':perfil, 'form':form}
        return render(request, 'mainapp/perfil.html', context)
    
@login_required(login_url='logueo')
def delete_perfil(request,user):
    if not request.user.is_authenticated:
        messages.error(request,'Tienes que iniciar sesion')
        return redirect('index')

    if Cliente.objects.filter(perfil=request.user).exists(): 
        cliente_delete= Cliente.objects.filter(perfil=request.user)
        cliente_delete.delete()

    elif Niñera.objects.filter(perfil=request.user).exists():
        niñera_delete= Niñera.objects.filter(perfil=request.user)
        niñera_delete.delete()
    else:
        messages.error(request,'No se puede acceder')
        return redirect('index')
    
    messages.success(request,'Perfil Eliminado Correctamente')
    return redirect('index')

def login_landing(request, cliente=None, niñera=None):
    if Cliente.objects.filter(perfil_id = request.user.id).exists():
        cliente = Cliente.objects.get(perfil_id = request.user.id)
    elif Niñera.objects.filter(perfil_id = request.user.id).exists():
        niñera = Niñera.objects.get(perfil_id = request.user.id)
    context = {'niñ':niñera,'cli':cliente}
    return render(request, 'mainapp/loginlanding.html', context)

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request,'Tienes que iniciar sesion')
        return redirect('index')
    if request.method == 'POST':
        searched = request.POST.get('search')
        buscar_cuidadoras = Niñera.objects.filter(titleicontains=searched)
    return render(request,'searcher.html',{
        'searched' : searched,
        'buscar_cuidadoras' : buscar_cuidadoras})
    
