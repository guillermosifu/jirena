from django.urls import path
from . import views

urlpatterns = [
    path('registros',views.TrackingRegistrosView.as_view(), name='registros')
]