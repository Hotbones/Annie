from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import NiñeraForm,ClienteForm,RegisterForm,ReservationForm
from .models import *

def index(request):
    if request.user.is_authenticated: 
        perfil_list = Cliente.objects.filter(perfil_cliente=request.user) 

        if perfil_list.exists():
            perfil_list = Cliente.objects.filter(perfil_cliente=request.user) 

        elif Niñera.objects.filter(perfil_niñera=request.user).exists():
            perfil_list = Niñera.objects.filter(perfil_niñera=request.user) 

        return render(request, 'mainapp/index.html', {
            'perfil_list' : perfil_list,
        })
    return render(request, 'mainapp/index.html', {
        })


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
            messages.success(request,'Bienvenido de nuevo'.format(usuario))
            return redirect('index')
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
    if Niñera.objects.filter(perfil_niñera=request.user).exists() or Cliente.objects.filter(perfil_cliente=request.user).exists():
        
            return redirect('index')
    form = NiñeraForm()


    if request.method == 'POST':
        
        form = NiñeraForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            form.perfil_niñera = user
            if not Cliente.objects.all():
                form.save()
                messages.success(request, message='Registro como niñera exitoso!')
                return redirect('index')  # access granted
                
            else:
                messages.error(request, message='Esta niñera ya se encuentra registrada')
                return redirect('index')    
            
        else:
            messages.error(request, message='Ha ocurrido un error con los campos a llenar.')

    return render(request, 'mainapp/register_niñera.html',{
        'form': form
    })

@login_required(login_url='logueo')
def register_cliente(request,user):

    if not request.user.is_authenticated:
        messages.error(request,'No se puede ir a la direccion')
        return redirect('index')
    if Niñera.objects.filter(perfil_niñera=request.user).exists() or Cliente.objects.filter(perfil_cliente=request.user).exists():
        
            return redirect('index')
    form = ClienteForm()


    if request.method == 'POST':
        
        form = ClienteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            form.perfil_cliente = user
            
            if not  Niñera.objects.all():
                form.save()
                messages.success(request, message='Registro como cliente exitoso!')
                return redirect('index')  # access granted
            else:
                return redirect('index')
           
            
        else:
            messages.error(request, message='Ha ocurrido un error con los campos a llenar.')
    else:
        form = ClienteForm()
    return render(request, 'mainapp/register_cliente.html', {'form_cliente':form})



@login_required(login_url='logueo')
def update_perfil(request,user):
    if Cliente.objects.all():
            perfil = Cliente.objects.get(perfil_cliente=request.user)
            form = ClienteForm(instance=perfil)
            if request.user != perfil.perfil_cliente:
                messages.success(request,'No estas autorizado')
            mod = Cliente.objects.get(perfil_cliente=request.user)

            messages.error(request,'No existe ningún perfil')

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success('Perfil actualizado exitosamente!')
            return redirect('index')

    
        context = {'perfil':perfil, 'form':form}
        return render(request, 'mainapp/perfil.html', context)
       
    messages.error(request,'Tienes que crear un perfil')
    return redirect('index')

def delete_perfil(request,cliente_id):
    if not request.user.is_authenticated:
        messages.error(request,'Tienes que iniciar sesion')
        return redirect('index')

    
    if Cliente.objects.all():
        
        if Cliente.objects.get(pk=cliente_id):
            cliente_delete= Cliente.objects.get(pk=cliente_id)
            cliente_delete.delete()
            messages.success(request,'Cliente Eliminada Correctamente')
    elif Niñera.objects.all():
        if Niñera.objects.get(pk=cliente_id):
            
                Niñera_delete= Niñera.objects.get(pk=cliente_id)
                Niñera_delete.delete()
                messages.success(request,'Niñera Eliminada Correctamente')
                return redirect('index')
    else:
        messages.error(request,'No puede acceder')
        
    return redirect('index')

       
def reserva_add(request,id):
    if request.user.is_authenticated:
        form = ReservationForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            user = User.objects.get(username=request.user.username)
            formulario.user_id = user

            id = Cliente.objects.get(id = id)
            formulario.sitter_publication =  id # refrencia al id de publicacion de sitter

            form.save()
            messages.success(request,'Reserva creada correctamente')
            return redirect('index')
    return render(request, 'mainapp/reservas.html',{
        'form' : form,
    })
        