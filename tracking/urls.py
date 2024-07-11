from django.urls import path
from . import views

app_name = 'tracking'

urlpatterns = [
    path("", views.index, name='index'),
    path("manifiesto",views.manifiesto,name='manifiesto'),
    path('login',views.auth_login, name='login'),
    path('logout',views.auth_logout, name='logout'),
    path('adjuntos/<int:tramo_id>',views.adjuntos,name='adjuntos'),
    path('imagenes/<int:tramo_id>',views.imagenes,name='imagenes')
]
