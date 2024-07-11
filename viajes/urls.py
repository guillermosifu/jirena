from django.urls import path
from . import views

app_name = 'viajes'

urlpatterns = [
    path("", views.index, name='index'),
    path('login',views.auth_login, name='login'),
    path('logout',views.auth_logout, name='logout'),
    path('catalogo/tipo_unidad',views.catalogo_tipo_unidad,name='veh_tipo_unidad'),
    path('catalogo/editar/<int:id>',views.catalogo_editar,name='cat_editar'),
    path('catalogo/desactivar/<int:id>',views.catalogo_desactivar,name='cat_desactivar')
]
