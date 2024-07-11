from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Q

from .models import (
    Clientes,Tramos,Guiarem,TrackingEstados,TrackingDestinatarios,
    TrackingManifiesto,Manifiestos,TrackingAdjuntos,TrackingRegistros
)

# Create your views here.
@login_required(login_url='/login')
def manifiesto(request):
    context = {}
    fecha_inicio = date(2023, 10, 1)
    cliente_tracking = Clientes.objects.get(pk=32)
    lista_destinatarios = TrackingDestinatarios.objects.filter(cliente=cliente_tracking)
    lista_estados = TrackingEstados.objects.all()
    lista = Manifiestos.objects.filter(rfcliente=cliente_tracking,fecha_creacion__gte=fecha_inicio).order_by('-id')
    filtered_tramos = lista

    filters = Q()
    
    if request.method == "POST":
        
        if request.POST['manifiesto'] != '':
            filters |= Q(curso=request.POST['manifiesto'])
    
        if request.POST['destinatario'] != '0':
            destinatario = TrackingDestinatarios.objects.get(pk=request.POST['destinatario'])
            filters |= Q(tracking__destinatario=destinatario)

        if request.POST['estado'] != '0':
            estado = TrackingEstados.objects.get(pk=request.POST['estado'])
            filters |= Q(tracking__estado=estado)
        #unidad_minera
        if request.POST['unidad_minera'] != '':
            filters |= Q(tracking__unidad_minera=request.POST['unidad_minera'])


    else:
        filters = Q(rfcliente=cliente_tracking,fecha_creacion__gte=fecha_inicio)
   
        
    filtered_tramos = Manifiestos.objects.filter(filters).order_by('-id')
    context = {
        'tramos':filtered_tramos,
        'destinatarios':lista_destinatarios,
        'estados':lista_estados
    }
    
    return render(request, 'manifiesto.html',context)

@login_required(login_url='/login')
def index(request):
    context = {}
    fecha_inicio = date(2023, 10, 1)
    cliente_tracking = Clientes.objects.get(pk=32)
    lista_destinatarios = TrackingDestinatarios.objects.filter(cliente=cliente_tracking)
    lista_estados = TrackingEstados.objects.all()
    lista_tramos = Tramos.objects.filter(cliente=cliente_tracking,fecha_creacion__gte=fecha_inicio,ntramo=1).order_by('-id')[:100]
    filtered_tramos = lista_tramos

    filters = Q()
    
    if request.method == "POST":
        if request.POST['manifiesto'] != '':
            filters |= Q(manif=request.POST['manifiesto'])

        if request.POST['destinatario'] != '0':
            destinatario = TrackingDestinatarios.objects.get(pk=request.POST['destinatario'])
            filters |= Q(tracking__destinatario=destinatario)

        if request.POST['estado'] != '0':
            estado = TrackingEstados.objects.get(pk=request.POST['estado'])
            filters |= Q(tracking__estado=estado)
        #unidad_minera
        if request.POST['unidad_minera'] != '':
            filters |= Q(tracking__glosa4=request.POST['unidad_minera'])


    else:
        filters = Q(cliente=cliente_tracking,fecha_creacion__gte=fecha_inicio)
   
        
    filtered_tramos = Tramos.objects.filter(filters,ntramo=1).order_by('-id')[:100]
    context = {
        'tramos':filtered_tramos,
        'destinatarios':lista_destinatarios,
        'estados':lista_estados
    }
    
    return render(request, 'index.html',context)

@login_required(login_url='/login')
def adjuntos(request,tramo_id):
    tramo = Tramos.objects.get(pk=tramo_id)
    print("tramo obj : ",tramo)
    context = {}
    if tramo is not None:
        tracking = TrackingRegistros.objects.filter(tramo=tramo).first()
        if tracking is not None:
            print("tracking obj : ",tracking)
            lista_adjuntos = TrackingAdjuntos.objects.filter(tracking=tracking)
    
            context = {
                'tracking':tracking,
                'adjuntos':lista_adjuntos
            }
    
    print(context)
    
    return render(request,'adjuntos.html',context)

@login_required(login_url='/login')
def imagenes(request,tramo_id):
    tramo = Tramos.objects.get(pk=tramo_id)
    print("tramo obj : ",tramo)
    context = {}
    if tramo is not None:
            context = {
                'tramo':tramo
            }
    
    print("context : ",context)
    return render(request,'imagenes.html',context)
    

def auth_login(request):
    if request.method == "POST":
        usuario = request.POST['usuario']
        password = request.POST['password']
        
        user_auth = authenticate(request,username=usuario,password=password)
        print(user_auth)
        if user_auth is not None:
            login(request,user_auth)
            return redirect('/')
        else:
            context = {
                'error':'datos invalidos'
            }
            return render(request,'login.html',context)
    
    return render(request,'login.html')

def auth_logout(request):
    logout(request)
    return redirect('/')