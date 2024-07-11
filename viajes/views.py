from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from datetime import date

from .models import (
    Grupo,Catalogo,Articulo
)

def auth_login(request):
    if request.method == "POST":
        usuario = request.POST['usuario']
        password = request.POST['password']
        
        user_auth = authenticate(request,username=usuario,password=password)
        print(user_auth)
        if user_auth is not None:
            login(request,user_auth)
            return redirect('/viajes')
        else:
            context = {
                'error':'datos invalidos'
            }
            return render(request,'login.html',context)
    
    return render(request,'viajes/login.html')

def auth_logout(request):
    logout(request)
    return redirect('/viajes/login')

@login_required(login_url='/viajes/login')
def index(request):
    context = {}
    return render(request, 'viajes/index.html',context)

@login_required(login_url='/viajes/login')
def catalogo_tipo_unidad(request):
    grupo = Grupo.objects.get(codigo='VEH_TIP_UNI')
    
    if request.method == "POST":
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']
        
        catalogo = Catalogo()
        catalogo.codigo = codigo
        catalogo.descripcion = descripcion
        catalogo.grupo = grupo
        catalogo.save()
    
    
    queryset = grupo.catalogo_set.filter(estado=1)
    context ={
        'listado':queryset
    }
    return render(request,'viajes/veh_tipo_unidad.html',context)

@login_required(login_url='/viajes/login')
def catalogo_editar(request,id):
    grupo = Grupo.objects.get(codigo='VEH_TIP_UNI')
    catalogo_editar = Catalogo.objects.get(pk=id)
    
    if request.method == "POST":
        codigo = request.POST['codigo']
        descripcion = request.POST['descripcion']
        catalogo_editar.codigo = codigo
        catalogo_editar.descripcion = descripcion
        catalogo_editar.save()
        
        return redirect('/viajes/catalogo/tipo_unidad')
    
    queryset = grupo.catalogo_set.filter(estado=1)
    print(queryset)
    context ={
        'listado':queryset,
        'cateditar':catalogo_editar
    }
    return render(request,'viajes/veh_tipo_unidad.html',context)

@login_required(login_url='/viajes/login')
def catalogo_desactivar(request,id):
    catalogo = Catalogo.objects.get(pk=id)
    catalogo.estado = 0
    catalogo.save()
    return redirect('/viajes/catalogo/tipo_unidad')
    
    


