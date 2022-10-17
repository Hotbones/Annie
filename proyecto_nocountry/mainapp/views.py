from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import NiñeraForm,ClienteForm,RegisterForm,MensajeForm
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
def perfil_niñera(request):
    niñeras = Niñera.objects.all()
    mi_perfil = Niñera.objects.get(perfil_id=request.user.id)
    context = {'niñeras':niñeras, 'mi_perfil':mi_perfil}
    return render(request, 'mainapp/perfilniñera.html', context)

@login_required(login_url='logueo')
def perfil_cliente(request):
    return render(request, 'mainapp/perfilcliente.html', {})

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

    if Niñera.objects.filter(perfil=request.user).exists() or \
        Cliente.objects.filter(perfil=request.user).exists():
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
   
    if Niñera.objects.filter(perfil=request.user).exists() or \
    Cliente.objects.filter(perfil=request.user).exists():
        messages.error(request, message='Ya has creado un perfil')
        return redirect('index')


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

            form.perfil = user
            # if not Cliente.objects.all():
            if form.perfil not in Cliente.objects.all():
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
        messages.error(request,'No existe ningún perfil')
        return redirect('index')
    finally:
        context = {'perfil':perfil, 'form':form}
        return render(request, 'mainapp/perfil.html', context)


       
# def reserva_add(request,id):
#     if request.user.is_authenticated:
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             formulario = form.save(commit=False)
#             user = User.objects.get(username=request.user.username)
#             formulario.user_id = user

#             id = Cliente.objects.get(id = id)
#             formulario.sitter_publication =  id # refrencia al id de publicacion de sitter

#             form.save()
#             messages.success(request,'Reserva creada correctamente')
#             return redirect('index')
#     return render(request, 'mainapp/reservas.html',{
#         'form' : form,
#     })
        
@login_required(login_url='logueo')
def crear_mensaje(request,pk):

    puntaje=0
    usuario = User.objects.get(id=pk)

    form = MensajeForm(instance=usuario)
    if request.method == 'POST':
        form = MensajeForm(request.POST, instance=usuario)
        if form.is_valid():
            comentarista = request.user.username
            puntaje=str(puntaje)
            nuevo_comentario = form.cleaned_data['mensaje']
            c = Mensaje(usuario=usuario, comentarista=comentarista, puntaje=puntaje, mensaje=nuevo_comentario)
            c.save()

            return redirect('index')
        else:
            print('form is invalid')

    else:
        form = MensajeForm()

    context = {'form':form, 'usuario':usuario}

    return render(request,'mainapp/crear_mensaje.html',context)
